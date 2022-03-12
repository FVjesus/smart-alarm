import lcddriver
import time

mylcd = lcddriver.lcd()

while True:
  mylcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
  mylcd.lcd_display_string(time.strftime('%a %b %d, 20%y'), 2)
