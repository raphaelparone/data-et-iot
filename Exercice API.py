import network   #import des fonction lier au wifi
import urequests#import des fonction lier au requetes http
import utime#import des fonction lier au temps
import ujson#import des fonction lier aà la convertion en Json
from machine import Pin, PWM
import random
wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'iPhone'
password = '123456789'
wlan.connect(ssid, password) # connecte la raspi au réseau
id_character = ['6afb1960-febd-418d-b604-e50c1b59459b', '43403619-70cb-4a0c-b70a-6d5cae20e602', 'ca3827f0-375a-4891-aaa5-f5e8a5bad225', '9055a7b1-6ac9-4363-977c-4dec78572fad', 'd5c4daa3-c726-426a-aa98-fb40f3fba816', 'c5acae3e-1a05-4f1d-bb83-3f8c7639d84e', '3569d265-bd27-44d8-88e8-82fb0a848374', '1cd6dc64-01a9-4379-9cfd-1a7167ba1bb1', '2cfd2d4b-5d1e-4dc5-8837-37a97c7e2f2f', '7cc5e694-850d-4c44-830b-7154e23bb5c3', '2772994f-6a19-4d01-9993-5e10cc6f69a5']

maisons = { "Gryffindor": [30000, 5, 5],
            "Slytherin": [5, 30000, 5],
            "Ravenclaw": [5, 5, 30000],
            "Hufflepuff": [30000, 30000, 5]
            }
pwm_ledR = PWM(Pin(13,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledR.freq(1_000)
pwm_ledG = PWM(Pin(14,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledG.freq(1_000)
pwm_ledB = PWM(Pin(15,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledB.freq(1_000)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass


while(True):
    try:
        print("GET")
        url = "https://hp-api.onrender.com/api/character/" + id_character[random.randint(0, len(id_character) - 1)]
        r = urequests.get(url) # lance une requete sur l'url
        maison = r.json()[0]["house"]
        r.close() # ferme la demande
        utime.sleep(1)
        pwm_ledR.duty_u16(maisons[maison][0])
        pwm_ledG.duty_u16(maisons[maison][1])
        pwm_ledB.duty_u16(maisons[maison][2])
        r.close() # ferme la demande
    except Exception as e:
        print(e)
