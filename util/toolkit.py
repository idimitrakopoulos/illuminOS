import time, gc

def log(msg):
    # TODO: Heavy to use ticks and concatenate each time. Need to find a better way
    print(str(time.ticks_ms()) + " [INFO] "  + str(msg))


def scan_wifi():
    import network

    n = network.WLAN(network.STA_IF)
    n.active(True)

    return n.scan()


def determine_preferred_wifi(configured, found):
    connect_to = {}
    for j in found:
        for k, v in configured.items():
            if j[0].decode('UTF-8') == k:
                log("Configured WiFi network '" + k + "' was found")
                connect_to = {"ssid" : k, "password" : v}

    return connect_to

def connect_to_wifi(ssid, password):
    import network
    log("Attempting to connect to WiFi '" + ssid + "' with password '" + password +"'...")
    n = network.WLAN(network.STA_IF)
    n.active(True)
    n.connect(ssid, password)

    return n.ifconfig()[0]

def blink_onboard_led(times, delay, led):
    import time

    # Do blinking
    for i in range(times):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)

    # Return to off state
    led.high()


def load_properties(filepath, sep='=', comment_char='#', section_char='['):
    """
    Read the file passed as parameter as a properties file.
    """
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not (l.startswith(comment_char) or l.startswith(section_char)):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value

    return props

def format_fs():
    import uos
    log("Formatting filesystem ...")

    while uos.listdir("/"):
        lst = uos.listdir("/")
        uos.chdir("/")
        while lst:
            try:
                uos.remove(lst[0])
                log("Removed '" + uos.getcwd() + "/" + lst[0] + "'")
                lst = uos.listdir(uos.getcwd())
            except:
                log("Non-empty directory '" + uos.getcwd() + "/" + lst[0] + "' detected. Opening it...")
                uos.chdir(lst[0])
                lst = uos.listdir(uos.getcwd())

    log("Format completed successfully")

button_click_counter = {}

def get_button_clicks(btn, bcc_key):
    from machine import Timer

    if (btn.value() == 0):
        global button_click_counter
        button_click_counter[bcc_key] += 1
        if button_click_counter[bcc_key] == 1:
            log("single-click registered (mem free: " + str(gc.mem_free()) + ")")
        elif button_click_counter[bcc_key] == 2:
            log("double click registered (mem free: " + str(gc.mem_free()) + ")")
        else:
            log("lots of clicks! (mem free: " + str(gc.mem_free()) + ")")

        gtim = Timer(1)
        gtim.init(period=300, mode=Timer.ONE_SHOT, callback=lambda t:reset_button_click_counter(bcc_key))

def reset_button_click_counter(bcc_key):
    global button_click_counter
    log("FBC resetting to 0. Previous was " + str(button_click_counter[bcc_key]))
    button_click_counter[bcc_key] = 0
    return button_click_counter[bcc_key]

def updateDuckDNS(domain, token, ip):
    pass

def sendInstapushNotification(app_id, app_secret, event, trackers):
    import urequests, json
    url = 'https://api.instapush.im/v1/post'
    headers = {'x-instapush-appid': app_id, 'x-instapush-appsecret': app_secret, 'Content-Type': "application/json"}
    data = '{"event": "' +  event + '", "trackers": ' + json.dumps(trackers) + '}'
    resp = urequests.post(url, data=data, headers=headers)

    return resp.json()