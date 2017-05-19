import time
import random

from subprocess import call
from gpiozero import LED, Button
from time import sleep
from signal import pause


led = LED(18)
button = Button(23)

# the function that choose what number of the zine to print by a random integer
def chooser():
        led.on()
        numRan = random.randint(0, 9)
        if numRan == 0:
                call("sudo lpr /home/pi/py_app/0.pdf",shell=True)
        elif numRan == 1:
                call("sudo lpr /home/pi/py_app/1.pdf",shell=True)
        elif numRan == 2:
                call("sudo lpr /home/pi/py_app/2.pdf",shell=True)
        elif numRan == 3:
                call("sudo lpr /home/pi/py_app/3.pdf",shell=True)
        elif numRan == 4:
                call("sudo lpr /home/pi/py_app/4.pdf",shell=True)
        elif numRan == 5:
                call("sudo lpr /home/pi/py_app/5.pdf",shell=True)
        elif numRan == 6:
                call("sudo lpr /home/pi/py_app/6.pdf",shell=True)
        elif numRan == 7:
                call("sudo lpr /home/pi/py_app/7.pdf",shell=True)
        elif numRan == 8:
                call("sudo lpr /home/pi/py_app/8.pdf",shell=True)
        else :
                        call("sudo lpr /home/pi/py_app/9.pdf",shell=True)
        sleep(20)
        led.off()

button.when_pressed = chooser


pause()
