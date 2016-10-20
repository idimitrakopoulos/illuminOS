# illuminOS

An open-source MicroPython based SDK for ESP8266 WiFi-enabled microcontrollers. 

Intended for use in both commercial and open-source projects.

### Main Features

* Enables you to focus on your actual project by providing ready-made functionality for tedious stuff 
* Handles connections with known Wi-Fi networks according to user-defined priority
* Detects single or any number of taps on microcontroller buttons and allows execution of any code after that
* Automated installation on the mirocontroller (see installation section using `mpfshell`)
* Filesystem formatter cleans up your microcontroller - no need to reflash it
* Simple logging functionality

## Resources

[![Build Status](https://travis-ci.org/idimitrakopoulos/illuminOS.svg?branch=master)](https://travis-ci.org/idimitrakopoulos/illuminOS)

Github issues list/bugtracker: https://github.com/idimitrakopoulos/illuminOS/issues

## Quick Install

Clone the git repository in any local directory by typing the following:

```bash
$ git clone https://github.com/idimitrakopoulos/illuminOS
$ cd illuminOS
```
Now you need to upload it to your microcontroller. To do this you can use the excellent `mpfshell` [see installation instructions here](https://github.com/wendlers/mpfshell). 

After installing mpfshell you should connect your PC and microntroller via USB and type:

```bash
$ sudo mpfshell -s mpf_cmd.mpf
```

Of course you can also upload `illuminOS` manually or using one of your favorite IDEs (e.g. ESPlorer) 

## Examples

### Connect to preferred Wi-Fi network

Simply edit `conf/network.properties` with WiFi SSID and password as shown below

```properties
[wifi]
mynetwork = "abcdef"
worknet = "2334d"
```

Then in `main.py` simply use the following code. This will scan for known SSIDs as per your configuration above and connect to the first preferred network

```python
from util.toolkit import log, load_properties, scan_wifi, determine_preferred_wifi, connect_to_wifi

configured_wifis = load_properties("conf/network.properties")
found_wifis = scan_wifi()
preferred_wifi = determine_preferred_wifi(configured_wifis, found_wifis)
ip = connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"])

log("Connected with IP: " + ip)
```


### Listen for button clicks

To listen for clicks on the Flash button of your board, place the following snippet in your `main.py`. This places a polling timer which anticipates button clicks. Upon first click it very briefly waits for another click and then registers either a single or a double click.

Following this you could execute any code required by your project.

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
