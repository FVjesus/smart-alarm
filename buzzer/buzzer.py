from gpiozero import Buzzer
from time import sleep

class alarmSound():

  def __init__(self):
    self.buzzer = Buzzer(17)

  def beep(self):
    self.buzzer.on()
    sleep(1)
    self.buzzer.off()
    sleep(1)
    self.buzzer.on()
    sleep(3)