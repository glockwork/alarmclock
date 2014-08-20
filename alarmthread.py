#21.07.14
#This class will be where the main thread used for the alarm will be
#import test
import threading
import time
import RPi.GPIO as GPIO

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours=int(hours)
        self.minutes = int(minutes)
        self.keep_running = True


    def run(self):
        try:
            print(self.minutes)
            while self.keep_running:
                now = time.localtime()
                
                print ("Inside loop")
                if(now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print ("Ring Ring")
                    var=1
                    print ("Start Loop")
                    while var <4 :
                        GPIO.setmode(GPIO.BOARD)
                        GPIO.setup(7,GPIO.OUT)
                        time.sleep(1)
                        print ("Set output to True")
                        GPIO.output(7,True)
                        time.sleep(1)
                        print ("Set output to False")
                        GPIO.output(7,False)
                        var+= 1
                    return
            time.sleep(30000)
                
        except:
            return
        def just_die(self):
            self.keep_running = False
                
                
if __name__ == '__main__':       
        alarm_HH = 17
        alarm_MM = 58

        alarm = Alarm(alarm_HH, alarm_MM)
        alarm.start()
