import network
import secrets
import urequests
from utime import sleep, ticks_ms, ticks_diff

print('Connecting to WiFi Network Name:', secrets.SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

start = ticks_ms() # start a millisecond counter

if not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print("Waiting for connection...")
    counter = 0
    while not wlan.isconnected():
        sleep(1)
        print(counter, '.', sep='', end='', )
        counter += 1

delta = ticks_diff(ticks_ms(), start)
print("Connect Time:", delta, 'milliseconds')
print("IP Address:", wlan.ifconfig()[0])

base = 'http://api.openweathermap.org/data/2.5/forecast?units=imperial&'
location = '5037649' # twin cities
url = base + 'id=' + location + '&appid=' + secrets.appid

weather = urequests.get(url).json()
print('City:', weather['city']['name'])
print('Timezone:', weather['city']['timezone'])

# this could be up to 39 values
max_items = 14
# print a row of dates and hours
for i in range(0, max_items):
    print(weather['list'][i]['dt_txt'][5:13], ' ', sep='', end='')
print()
# print a row of temperatures
for i in range(0, max_items):    
    print(round(weather['list'][i]['main']['temp']), '      ', end='')
    # print('feels like:', weather['list'][i]['main']['feels_like'])
    # print(weather['list'][i]['weather'][0]['description'])
    # print(weather['list'][i]['dt_txt'])
    
# print(weather)