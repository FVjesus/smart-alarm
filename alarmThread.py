import time
import threading

from buzzer import buzzer

class alarmThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.sound = buzzer.alarmSound()
    self.stopping = False
  
  def stop(self):
    self.stopping = True

  def run(self): 
    while(not self.stopping):
      self.sound.beep()
      time.sleep(5)
    