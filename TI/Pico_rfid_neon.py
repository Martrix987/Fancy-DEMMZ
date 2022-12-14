from mfrc522 import MFRC522
import utime
import time
import machine
import neopixel

#Alle RFID ID's die zijn goedgekeurd
RFID_ID = [3655024877, 380337338]
neon = neopixel.NeoPixel(machine.Pin(13), 8)
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
temp = 0

print("Bring TAG closer...")
print("")


while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            neon[0] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[1] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[2] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[3] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[4] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[5] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[6] = [0, 0, 50]
            time.sleep(0.1)
            neon.write()
            neon[7] = [0, 0, 50]
            neon.write()
            time.sleep(0.1)
            
            
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
            print(str(uid))
            if card in RFID_ID:
                print('autorized')
                neon[0] = [0, 50, 0]
                neon[1] = [0, 50, 0]
                neon[2] = [0, 50, 0]
                neon[3] = [0, 50, 0]
                neon[4] = [0, 50, 0]
                neon[5] = [0, 50, 0]
                neon[6] = [0, 50, 0]
                neon[7] = [0, 50, 0]
                neon.write()
                time.sleep(1)
                neon[0] = [0, 0, 0]
                neon[1] = [0, 0, 0]
                neon[2] = [0, 0, 0]
                neon[3] = [0, 0, 0]
                neon[4] = [0, 0, 0]
                neon[5] = [0, 0, 0]
                neon[6] = [0, 0, 0]
                neon[7] = [0, 0, 0]
            else:
                print('not')
                neon[0] = [50, 0, 0]
                neon[1] = [50, 0, 0]
                neon[2] = [50, 0, 0]
                neon[3] = [50, 0, 0]
                neon[4] = [50, 0, 0]
                neon[5] = [50, 0, 0]
                neon[6] = [50, 0, 0]
                neon[7] = [50, 0, 0]
                neon.write() 
                time.sleep(1)
                neon[0] = [0, 0, 0]
                neon[1] = [0, 0, 0]
                neon[2] = [0, 0, 0]
                neon[3] = [0, 0, 0]
                neon[4] = [0, 0, 0]
                neon[5] = [0, 0, 0]
                neon[6] = [0, 0, 0]
                neon[7] = [0, 0, 0]
            


utime.sleep_ms(500)



