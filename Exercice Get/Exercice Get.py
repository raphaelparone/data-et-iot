import network
import urequests
import utime
import ujson
from machine import Pin, PWM
import random

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'iPhone'
password = '123456789'
wlan.connect(ssid, password)
maisons = {
    "Gryffindor": [30000, 5, 5],
    "Slytherin": [5, 30000, 5],
    "Ravenclaw": [5, 5, 30000],
    "Hufflepuff": [30000, 30000, 5]
}

pwm_ledR = PWM(Pin(13, mode=Pin.OUT))
pwm_ledR.freq(1000)
pwm_ledG = PWM(Pin(14, mode=Pin.OUT))
pwm_ledG.freq(1000)
pwm_ledB = PWM(Pin(15, mode=Pin.OUT))
pwm_ledB.freq(1000)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)

while True:
    try:
        print("GET")
        card_id = random.randint(0, len(id_character) - 1)
        url = "https://hp-api.onrender.com/api/character/".format(card_id)
        r = urequests.get(url)
        data = r.json()
        maison = data['house']
        r.close()
        utime.sleep(1)
        
        pwm_ledR.duty_u16(maisons[maison][0])
        pwm_ledG.duty_u16(maisons[maison][1])
        pwm_ledB.duty_u16(maisons[maison][2])
        
    except Exception as e:
        print(e)
