from lib.Stepper import Stepper
from lib.PropertyManager import PropertyManager
import machine
from lib.toolkit import log

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    log.info("Woke from deep sleep ...")
else:
    log.info("Power on from hard reset ...")

p = PropertyManager("conf/profile.properties")
stepper = Stepper(p.get_str_property("step_file"), 2)

if stepper.get_current_step() == 1:
    log.debug("step 1 code")

    from hw.screen.SSD1306 import SSD1306
    from hw.screen.Screen import ConnectionType
    from hw.sensor.AnalogSensor import AnalogSensor

    log.debug("Connecting to soil humidity sensor at pin {}".format(p.get_str_property("analog_pin")))

    # SUBMERGED IN WATER (vlow)   : 364
    # COMPLETELY DRY     (vhigh)  : 1024
    soil_sensor = AnalogSensor(p.get_int_property("analog_pin"),
                               p.get_int_property("vhigh"),
                               p.get_int_property("vlow"))

    # SSD1306 OLED init
    log.debug("Connecting to SSD1306 OLED Screen at scl: {}, sda: {}".format(p.get_str_property("ssd1306_scl"),
                                                                             p.get_str_property("ssd1306_sda")))
    bus = machine.I2C(freq=400000,
                      scl=machine.Pin(p.get_int_property("ssd1306_scl")),
                      sda=machine.Pin(p.get_int_property("ssd1306_sda")))

    oled = SSD1306(ConnectionType.I2C, bus)

    shumidity = soil_sensor.get_value()

    log.info("Soil humidity sensor value is {}".format(shumidity))
    oled.text("Soil Humidity")
    oled.text("{}".format(shumidity), 0, 10)

    step_file_dict = {'current_step': '2',
                      'shumidity' : shumidity}

    stepper.create_property_file(p.get_str_property("step_file"), step_file_dict)

    log.info("End of step '{}'. Rebooting board ...".format(str(stepper.get_current_step())))
    import utime
    utime.sleep_ms(2000)
    machine.reset()

elif stepper.get_current_step() == 2:
    log.debug("step 2 code")
    import gc
    from hw.board.NodeMCU import NodeMCU
    from lib.toolkit import send_instapush_notification, determine_preferred_wifi, load_properties

    gc.collect()
    log.debug(gc.mem_free())
    board = NodeMCU()

    preferred_wifi = determine_preferred_wifi(load_properties("conf/network.properties"), board.scan_wifi())
    gc.collect()
    log.debug(gc.mem_free())

    ip = board.connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"], 10)
    gc.collect()
    log.debug(gc.mem_free())


    import urequests

    url = 'http://haxae.com:8086/write?db=plant_monitor'
    payload = 'plants,plant_name=pachira shumidity={}'.format(stepper.prop_manager.get_str_property("shumidity"))
    headers = {'X-Requested-With': 'Python requests', 'Content-type': 'text/xml'}
    r = urequests.post(url, data=payload, headers=headers)

    gc.collect()
    log.debug(gc.mem_free())

    stepper.remove_property_file(p.get_str_property("step_file"))

    log.info("End of step '{}'. Sleeping ...".format(str(stepper.get_current_step())))
    # Wake every 6 hours a.k.a 4 times/day
    board.sleep(21600000)


else:
    pass

