#21.07.14
#This class will be where the main thread used for the alarm will be
import test
import threading
import time

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
                    test.Ring()
                    return
            time.sleep(60000)
                
        except:
            return
        def just_die(self):
            self.keep_running = False
                
                
if __name__ == '__main__':       
        alarm_HH = 15
        alarm_MM = 41

        alarm = Alarm(alarm_HH, alarm_MM)
        alarm.start()
