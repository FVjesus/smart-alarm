from gpiozero import Buzzer
from time import sleep

class alarmSound():

  def __init__(self):
    self.buzzer = Buzzer(17)
    self.stop = False

  def stop(self):
    self.stop = True

  def beep(self):
    i = 2
    while (i > 0):
      i-= 1
      self.buzzer.on()
      sleep(1/100)
      self.buzzer.off()
      sleep(1/5)
      self.buzzer.on()
      sleep(3/10)
      self.buzzer.off()