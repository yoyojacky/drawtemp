from liquidcrystal_i2c import LCD
import subprocess as sp
from time import sleep


lcd = LCD(bus=1, addr=0x27, cols=20, rows=4)
lcd.clear()
lcd.home()
while True:
    lcd.backlight()
    temp = sp.getoutput("vcgencmd measure_temp")
    ip = sp.getoutput("hostname -I")
    lcd.setCursor(1,0)
    lcd.print("Hello, world!")
    lcd.setCursor(1,1)
    lcd.print(temp)

    lcd.setCursor(1,2)
    lcd.print("IP:{}".format(ip))

    lcd.setCursor(1,3)
    lcd.print("GeeekPi is Great!")
    sleep(1)
    lcd.noBacklight()
    sleep(1)

