import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
# simple while loop to turn the bell off and on


var=1
print ("Start Loop")
while var ==1 :
    print ("Set output to False")
    GPIO.output(7,False)
    time.sleep(1)
    print ("Set output to True")
    GPIO.output(7,True)
    time.sleep(1)
