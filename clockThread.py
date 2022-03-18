import time
import threading
from gpiozero import Button
from datetime import datetime, timedelta

from buzzer import buzzer
from lcd import lcddriver

class clockThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.lcd = lcddriver.lcd()
    self.stopping = False
  
  def stop(self):
    self.stopping = True

  def run(self):
    start = False
    stopBeep = False
    buttonA = Button(27)
    buttonB = Button(22)
    buttonC = Button(23)
    buttonD = Button(24)

    nextAlarm = datetime(1, 1, 1, 0, 0)
    sound = buzzer.alarmSound()

    self.lcd.lcd_display_string("Welcome! :)", 1)
    time.sleep(2)
    self.lcd.lcd_display_string("You need to choose", 1)
    self.lcd.lcd_display_string("your alarm...",2)
    time.sleep(1)

    while(not start):
      string = "*My Alarm* "
      string += nextAlarm.strftime('%H:%M')
      self.lcd.lcd_display_string(string, 4)

      if buttonA.is_pressed:
        self.lcd.clear()
        start = True
        self.lcd.lcd_display_string("Starting! :)", 1)
        time.sleep(2)
      
      if buttonB.is_pressed:
        self.lcd.lcd_display_string("+ 5mim in alarm", 3)
        nextAlarm = nextAlarm + timedelta(minutes = 5)
        time.sleep(1/2)
        self.lcd.lcd_display_string("", 3)
      
      if buttonC.is_pressed:
        self.lcd.lcd_display_string("+ 30mim in alarm", 3)
        nextAlarm = nextAlarm + timedelta(minutes = 30)
        time.sleep(1/2)
        self.lcd.lcd_display_string("", 3)
      
      if buttonD.is_pressed:
        self.lcd.lcd_display_string("+ 1hour in alarm", 3)
        nextAlarm = nextAlarm + timedelta(minutes = 60)
        time.sleep(1/2)
        self.lcd.lcd_display_string("", 3)
      
    while(not self.stopping):
      string = "*Next Alarm* "
      string += nextAlarm.strftime('%H:%M')

      self.lcd.lcd_display_string(time.strftime('%H:%M'), 1)
      self.lcd.lcd_display_string(time.strftime('%a %b %d, 20%y'), 2)
      self.lcd.lcd_display_string(string, 4)

      if buttonA.is_pressed:
        if not stopBeep:
          stopBeep = not stopBeep
          self.lcd.lcd_display_string("Have a nice day! :)", 3)
          time.sleep(2)
          self.lcd.lcd_display_string("", 3)
    
      if buttonB.is_pressed:
        self.lcd.lcd_display_string("+ 5mim in alarm", 3)
        nextAlarm = nextAlarm + timedelta(minutes = 5)
        time.sleep(1)
        self.lcd.lcd_display_string("", 3)
        stopBeep = False
      
      if buttonC.is_pressed:
        self.lcd.lcd_display_string("+ 30mim in alarm", 3)
        nextAlarm = nextAlarm + timedelta(minutes = 30)
        time.sleep(1)
        self.lcd.lcd_display_string("", 3)
        stopBeep = False
      
      if buttonD.is_pressed:
        self.lcd.lcd_display_string("+ 1hour in alarm", 3)
        nextAlarm = nextAlarm + timedelta(minutes = 60)
        time.sleep(1)
        self.lcd.lcd_display_string("", 3)
        stopBeep = False
      
      if not stopBeep and nextAlarm.strftime('%H:%M') == datetime.now().strftime('%H:%M'):
        self.lcd.lcd_display_string("Wake Up!", 3)
        sound.beep()
        self.lcd.lcd_display_string("",3)
    
    self.lcd.clear()
    self.lcd.lcd_display_string("Bye Bye!", 1)
    time.sleep(1)
    self.lcd.lcd_display_string("See you later!",2)
    time.sleep(2)
    self.lcd.clear()
