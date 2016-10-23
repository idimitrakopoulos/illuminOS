from lib.Kernel import Kernel

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
                log.info("Configured WiFi network '" + k + "' was found")
                connect_to = {"ssid" : k, "password" : v}

    return connect_to

def connect_to_wifi(ssid, password, wait_for_ip=0):
    import network, time
    log.info("Attempting to connect to WiFi '" + ssid + "' with password '" + password +"'...")
    n = network.WLAN(network.STA_IF)
    n.active(True)
    n.connect(ssid, password)

    # Wait for IP address to be provided
    count = 0
    while not n.isconnected() and count < wait_for_ip:
        log.info("Waiting to obtain IP ... (" + str(wait_for_ip - count) + " sec remaining)" )
        time.sleep(1)
        count += 1

    # Get provided IP
    ip = n.ifconfig()[0]

    if ip == "0.0.0.0":
        log.info("Could not obtain IP on '" + ssid + "'")
    else:

        log.info("Connected with IP '" + ip + "'")

    return ip


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


def update_duck_dns(domain, token, ip):
    log.info("Updating DuckDNS service. (Domain: '" + domain + "' IP: '" + ip + "')")
    http_get("https://www.duckdns.org/update?domains=" + domain + "&token=" + token + "&ip=" + ip)

def send_instapush_notification(app_id, app_secret, event, trackers):
    import urequests, json
    url = 'https://api.instapush.im/v1/post'
    headers = {'x-instapush-appid': app_id, 'x-instapush-appsecret': app_secret, 'Content-Type': "application/json"}
    data = '{"event": "' +  event + '", "trackers": ' + json.dumps(trackers) + '}'
    resp = urequests.post(url, data=data, headers=headers)

    return resp.json()

def http_get(url, debug=True):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True and debug:
        data = s.recv(100)
        if data:
            log.debug(str(data, 'utf8'))
        else:
            break

# Initialize
kernel = Kernel(load_properties("conf/os.properties"))
log = kernel.logger