import time
import threading

from lcd import lcddriver

class clockThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.lcd = lcddriver.lcd()
    self.stopping = False
  
  def stop(self):
    self.lcd.lcd_clear()
    self.stopping = True
  
  def run(self):
    while(not self.stopping):
      self.lcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
      self.lcd.lcd_display_string(time.strftime('%a %b %d, 20%y'), 2)