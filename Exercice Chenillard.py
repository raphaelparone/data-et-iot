from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber1 = 17 # declaration d'une variable pinNumber à 17
led1 = Pin(pinNumber1, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber2 = 21
led2 = Pin(pinNumber2, mode=Pin.OUT)
pinNumber3 = 27
led3 = Pin(pinNumber3, mode=Pin.OUT)

while True:          # boucle infini
    led1.on()         #allume la led 
    utime.sleep(0.1)   # attendre 1 seconde 
    led1.off()        #eteindre la led
    led2.on()
    utime.sleep(0.1)
    led2.off()
    led3.on()
    utime.sleep(0.1)
    led3.off()