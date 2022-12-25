import RGB1602
import time
lcd = RGB1602.RGB1602(16, 2)

#heart = bytearray([0x00, 0x00, 0x1B, 0x1F, 0x1F, 0x0E, 0x04, 0x00])
#test = bytearray([0x00])



lcd.set_color_white()
lcd.at(0,0).printout("Hello world.")
lcd.at(0,1).printout("2e regel") 


x = True
while x == True:
    lcd.set_rgb(255, 0, 0)
    time.sleep(1)
    lcd.set_rgb(0, 255, 0)
    time.sleep(1)
    lcd.set_rgb(0, 0, 255)
    time.sleep(1)
    lcd.set_rgb(0, 0, 0)

"""
From the LCD1602 RGB Module datasheet:
Operating voltage: 3.3 ~ 5V,  LCD controller: AiP31068
Communication Interface: I2C, RGB driver:     PCA9633
Display Panel character LCD,  Display size: 64.5 × 16.0mm
Characters: 16 × 2, Dimensions: 87.0 × 32.0 × 13.0mm
Backlight colors: 16M, Operating temperature: -20 ~ +70℃
"""



