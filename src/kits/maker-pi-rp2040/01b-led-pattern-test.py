# Demo for Maker Pi RP2040 board

import machine
import time

blue_led_pins = [0, 1, 2, 3,  4,  5,  6,  7, 16, 17, 26, 27, 28]
number_leds = len(blue_led_pins)
led_ports = []
delay = .05

# create a list of the ports
for i in range(number_leds):
   led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

while True:
    # blue up
    for i in range(0, number_leds):
        led_ports[i].high()
        time.sleep(delay)
        led_ports[i].low()
    # blue down
    for i in range(number_leds - 1, 0, -1):
        led_ports[i].high()
        time.sleep(delay)
        led_ports[i].low()
