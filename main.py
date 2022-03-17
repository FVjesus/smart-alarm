import time

import clockThread
import alarmThread

class smartAlarm:
  def __init__(self): 
    self.stopping = False
  
  def stop(self):
    self.stopping = True
  
  def execute(self):
    print("Starting smart alarm...")

    print("Loading clock...")
    clock = clockThread.clockThread()
    clock.setDaemon(True)

    print("Loading alarm...")
    alarm = alarmThread.alarmThread()
    alarm.setDaemon(True)

    print("Starting clock")
    clock.start()

    print("Starting alarm")
    alarm.start()

    try:
      while(self.stopping is False):
        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
      print("Interrupted, shutting down")
    
    print("Stopping all services")
    clock.stop()
    alarm.stop()

    print("Shutdow complet, now exiting")

    time.sleep(5) #To give threads time to shut down

alarm = smartAlarm()
alarm.execute()