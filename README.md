# illuminOS

An open-source MicroPython based SDK for ESP8266 WiFi-enabled microcontrollers. It enables you to focus on your actual project by providing ready-made functionality for tedious stuff

## Main Features

* Handles connections with known Wi-Fi networks according to user-defined priority
* Detects single or any number of taps on microcontroller buttons and allows execution of any code after that
* Allows the user to take control of the on-board LEDs and blink them with any pattern and delay
* Automated installation on the mirocontroller (see installation section using `mpfshell`)
* Filesystem formatter cleans up your microcontroller - no need to reflash it
* Can be configured for any microcontroller (currently supported `NodeMCU`)
* Simple logging functionality
* Ability to read .properties files for configuration
* Intended for use in both commercial and open-source projects.

## Resources

Github issues list/bugtracker: https://github.com/idimitrakopoulos/illuminOS/issues

## Quick Install

Clone the git repository in any local directory by typing the following:

```bash
$ git clone https://github.com/idimitrakopoulos/illuminOS
$ cd illuminOS
```
Now you need to upload it to your microcontroller. To do this you can use the excellent `mpfshell` [see installation instructions here](https://github.com/wendlers/mpfshell#installing). 

After installing mpfshell you should connect your PC and microntroller via USB and type:

```bash
$ sudo mpfshell -s mpf_cmd.mpf
```

Of course you can also upload `illuminOS` manually or using one of your favorite IDEs (e.g. ESPlorer) 

## Project Structure

A quick folder/file walkthrough of the project

```bash
conf (all configuration files go here)
  network.properties (define your wifi networks here)
util (utilities folder)
  nodemcu.py (hardware mapping of NodeMCU board)
  <yourboard.py> (you can write your own board mapping!)
  toolkit.py (a generic toolkit library that contains board agnostic functions)
boot.py (gets executed first during boot-up)
main.py (gets executed second)
```
The user is free to utilize the functionalitu offered by illuminOS freely and at any point. It certainly makes sense however to play with some of the examples below by adding code inside `main.py` or `boot.py`.

## Microcontroller Support

illuminOS is open enough to allow the configuration and control of any ESP based microcontroller. At this point only nodeMCU has been configured by the author but other controllers can be contributed by users. 

To do this a new module must be created.

e.g. `util/nodemcu.py`

In this file _board_ related configuration can be mapped and toolkit functions invoked. The concept is to abstract hardware mapping as much as possible from functionality.

## Examples

### Connect to preferred Wi-Fi network

Simply edit `conf/network.properties` with WiFi SSID and password as shown below

```properties
[wifi]
mynetwork = "abcdef"
worknet = "2334d"
```

Then in `main.py` the following code must be copied. This will scan for known SSIDs as per the configuration above and connect to the first preferred network

```python
from util.toolkit import log, load_properties, scan_wifi, determine_preferred_wifi, connect_to_wifi

configured_wifis = load_properties("conf/network.properties")
found_wifis = scan_wifi()
preferred_wifi = determine_preferred_wifi(configured_wifis, found_wifis)
ip = connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"])

log("Connected with IP: " + ip)
```
---

### Listen for button clicks

To listen for clicks on the Flash button of your board, place the following snippet in your `main.py`. This places a polling timer which anticipates button clicks. Upon first click it very briefly waits for another click and then registers either a single or a double click.

Following this event you could execute any code required by your project.

For the **Flash** button use

```python
import util.nodemcu as board
board.get_flash_button_interrupts()
```
And for the **User** button use 

```python
import util.nodemcu as board
board.get_user_button_interrupts()
```

---

### Control LEDs

You can make the on-board LEDs flash as per requirement by using the following command.

```python
import util.nodemcu as board
board.blink_blue_led(15, 0.06)
```

---

### Format "Filesystem"

You can recursively wipe files and folders from your microcontroller using this function. 

```python
from util.toolkit import format_fs
format_fs()
```
---

### Read .properties files

In case you want to provide configuration using .properties files you can use the illuminOS method `load_properties`

```python
from util.toolkit import load_properties
load_properties("conf/my.properties")
```
---

### Logging

A simple logging functionality exists  

```python
from util.toolkit import log
log("hello world!")
```

# License

The content of this project itself is licensed under the [Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/us/deed.en_US), and the underlying source code used to format and display that content is licensed under the [MIT license](http://opensource.org/licenses/mit-license.php).



Enjoy!

Iason D.
