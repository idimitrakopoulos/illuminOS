# illuminOS

An open-source MicroPython based OS for WiFi-enabled microcontrollers.
It enables you to focus on your actual project by providing ready-made functionality for tedious stuff.

## Main Features

* Handles connections with known Wi-Fi networks according to user-defined priority
* Detects single or any number of taps on microcontroller buttons and allows execution of any code after that
* Allows the user to take control of the on-board LEDs and blink them with any pattern and delay
* Automated installation on the mirocontroller (see installation section using `mpfshell`)
* Filesystem formatter cleans up your microcontroller - no need to reflash it
* Send (Insta)Push notifications to your mobile phone straight from your microcontroller
* Update a Dynamic DNS service (DuckDNS) so that your microcontroller is always available online
* Can be configured for (potentially) any MicroPython enabled microcontroller (out of the box support for `NodeMCU`)
* Simple logging functionality
* Ability to read .properties files for configuration
* Memory manager that periodically calls garbage collector
* Intended for use in both commercial and open-source projects.

## Resources

Github issues list/bugtracker: https://github.com/idimitrakopoulos/illuminOS/issues

## Quick Install

Clone the git repository in any local directory by typing the following:

```bash
$ git clone https://github.com/idimitrakopoulos/illuminOS
```
Now you need to upload it to your microcontroller. To do this first ensure you have the latest MicroPython firmware installed (>1.8.x). To upload files/folders you can use the excellent `mpfshell` [see installation instructions here](https://github.com/wendlers/mpfshell#installing). 

After installing mpfshell you should connect your PC and microntroller via USB and type (provided the device connects to `/dev/ttyUSB0`):

```bash
$ cd illuminOS
$ sudo mpfshell -s upload.mpf
```
If the device connects to another path then simply edit `upload.mpf` and replace `/dev/ttyUSB0` to the proper device before running the above command.

Of course you can also upload `illuminOS` manually or using one of your favorite IDEs (e.g. ESPlorer) 

## Project Structure

Both boot strap files `main.py` and `boot.py` are intentionally left empty.

The user is free to utilize the functionality offered by illuminOS freely and at any point. It certainly makes sense however, to play with some of the examples below.

## Microcontroller Support

illuminOS is open enough to allow the configuration and control of any ESP based microcontroller. At this point only nodeMCU has been configured by the author but other controllers can be contributed by users. 

To do this a new board class must be created that inherits from hw.Board.

e.g. `hw/NodeMCU.py`

In this class _board_ related configuration can be mapped and Board functions invoked. The concept is to abstract hardware mapping as much as possible from functionality.

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
from hw.board.NodeMCU import NodeMCU

# Instantiate our board
board = NodeMCU()

# Find preferred wifi
preferred_wifi = determine_preferred_wifi(load_properties("conf/network.properties"), board.scan_wifi())

# Get IP
ip = board.connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"], 10)


```
---

### Listen for button clicks

To listen for clicks on the Flash button of your board, place the following snippet in your `main.py`. This places a polling timer which anticipates button clicks. Upon first click it very briefly waits for another click and then registers either a single or a double click.

Following this event you could execute any code required by your project on single or double click (you need to specify this function in `lib.toolkit` module).

For the **Flash** button use

```python
from hw.board.NodeMCU import NodeMCU

# Instantiate our board
board = NodeMCU()

# Listen for events on FLASH button and run "hello_world" function on single and double click
board.get_flash_button_events("hello_world", "hello_world")

```
And for the **User** button use 

```python
# Listen for events on USER button and run "hello_world" function on single and double click
board.get_user_button_events("hello_world", "hello_world")
```

---

### Control LEDs

You can make the on-board LEDs flash as per requirement by using the following command.

```python
from hw.board.NodeMCU import NodeMCU

# Instantiate our board
board = NodeMCU()

# Blink BLUE LED 5 times with 0.5 sec delay
board.blink_blue_led(5, 0.5)

```

---

### Format "Filesystem"

You can recursively wipe files and folders from your microcontroller using this function. 

```python
from hw.board.NodeMCU import NodeMCU

# Instantiate our board
board = NodeMCU()

# Request format - this will wipe all the filesystem
board.format()

```
---

### Send (Insta)Push Notifications

You can use the InstaPush service to send push notifications to your mobile phone.

+ Go to the [Instapush](https://instapush.im) website and create an account. 
+ Download the Instapush app on your phone and login there as well
+ Once inside go to dashboard and create a new "application", give any name you like
+ In your new application create a new event
+ For the sake of this example name it "send_ip" (it can be anything you choose really)
+ Add a tracker called "ip"
+ Formulate your message as such "Hello, my IP address is {ip}"
+ Save it and make note of your app ID and app Secret
* Add the following to your code

```python
from lib.toolkit import sendInstapushNotification
r = sendInstapushNotification("57f65af3455ag7848a96876hjf077c3", "ea456d8c303be4shhg56669339ca43b8", "send_ip", {'ip': ip})
```
---

### Update Dynamic DNS (DuckDNS)

You can use the InstaPush service to send push notifications to your mobile phone.

+ Go to the [DuckDNS](https://duckdns.org) website and create an account. 
+ Once inside go to dashboard and create a new "domain", give any name you like
+ Save it and make note of your token id
* Add the following to your code

```python
from lib.toolkit import update_duck_dns

# Update DuckDNS service
update_duck_dns("mydomain", "mytoken", "192.168.0.10")
```
---

### Read .properties files

In case you want to provide configuration using .properties files you can use the illuminOS method `load_properties`

```python
from lib.toolkit import load_properties
load_properties("conf/my.properties")
```
---

### Memory Manager

Garbage collection is better performed before it's needed, the memory manager periodically runs and collects garbage plus it reports if memory is low

```python
from hw.board.NodeMCU import NodeMCU
# Instantiate our board
board = NodeMCU()

# Memory collection and reporting will occur every 10 sec
board.start_memory_manager(10000)

# Or you can run memory manager ad hoc
board.mem_cleanup()
```
---

### Logging

A simple logging functionality exists  

```python
import gc

from lib.Logger import Logger
log = Logger()

log.info("Hello!")
log.error("Critical Issue!!")
log.debug("Free memory: " + str(gc.free_mem()))
```

# License

The content of this project itself is licensed under the [Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/us/deed.en_US), and the underlying source code used to format and display that content is licensed under the [MIT license](http://opensource.org/licenses/mit-license.php).



Enjoy!

Iason D.
