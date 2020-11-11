# Autor: Gernot Huber
# Datei: Matrixtastatur

# einfaches Programm zur Bedienung einer 4x4-Matrixtastatur


import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setmode(GPIO.BOARD)

listekeys =  [['1','2','3','A'], ['4','5','6','B'], ['7','8','9','C'], ['*','0','#','D']]
keys = np.array(listekeys)

rowsPins = [12,16,18,22]        #row und korrespondierende pin:   r8=12,r7=16,r6=18,r5=22 
colsPins = [19,15,13,11]        #colum und korrespondierende pin: c1=11,c2=13,c3=15,c4=19

rpback = -1

for rp in rowsPins:
    GPIO.setup(rp,GPIO.IN, pull_up_down=GPIO.PUD_UP)
for cp in colsPins:
    GPIO.setup(cp,GPIO.OUT, initial=GPIO.HIGH)

def buttonEvent(channel):#Funktion wird ausgeführt, wenn Taste gedrückt
    global rpback
    global indexrp
    rpback = channel
    indexrp = rowsPins.index(channel)

for rp in rowsPins:
    GPIO.add_event_detect(rp,GPIO.FALLING,callback = buttonEvent,bouncetime=3000)

try:
    while True:
        for cp in colsPins:
            GPIO.output(cp, GPIO.LOW)
            time.sleep(0.1)
            if rpback != -1:
                indexcp = colsPins.index(cp)
                print (keys[indexrp, indexcp])
            rpback = -1
            GPIO.output(cp, GPIO.HIGH)
except KeyboardInterrupt:
    pass
print ("\nEnde")
GPIO.cleanup()
