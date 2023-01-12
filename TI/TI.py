from mfrc522 import MFRC522
import utime
import time
import machine
import neopixel

#Alle RFID ID's die zijn goedgekeurd
neon = neopixel.NeoPixel(machine.Pin(13), 8)
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
temp = 0


def red_neon_led():
    neon[0] = [50, 0, 0]
    neon[1] = [50, 0, 0]
    neon[2] = [50, 0, 0]
    neon[3] = [50, 0, 0]
    neon[4] = [50, 0, 0]
    neon[5] = [50, 0, 0]
    neon[6] = [50, 0, 0]
    neon[7] = [50, 0, 0]
    neon.write()
    
def green_neon_led():
    neon[0] = [0, 50, 0]
    neon[1] = [0, 50, 0]
    neon[2] = [0, 50, 0]
    neon[3] = [0, 50, 0]
    neon[4] = [0, 50, 0]
    neon[5] = [0, 50, 0]
    neon[6] = [0, 50, 0]
    neon[7] = [0, 50, 0]
    neon.write()
    
def black_neon_led():
    neon[0] = [0, 0, 0]
    neon[1] = [0, 0, 0]
    neon[2] = [0, 0, 0]
    neon[3] = [0, 0, 0]
    neon[4] = [0, 0, 0]
    neon[5] = [0, 0, 0]
    neon[6] = [0, 0, 0]
    neon[7] = [0, 0, 0]
    neon.write()

def loading_neon_led():
    neon[0] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[1] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[2] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[3] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[4] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[5] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[6] = [0, 0, 50]
    time.sleep(0.05)
    neon.write()
    neon[7] = [0, 0, 50]
    neon.write()
    time.sleep(0.125)

RFID_ID = [3655024877, 380337338]
def id_check(card):
    if card == 3655024877:
        return (76561198873808910)
    else:
        print('Error (steam id not linked to card yet)')

    
    
    
    

black_neon_led()
print("Bring TAG closer... \n")


while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            loading_neon_led()
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
            #print(str(uid))
            if card in RFID_ID:
                print(id_check(card))
                green_neon_led()
                time.sleep(2)
                black_neon_led()
                
            else:
                print('Wrong or unrecognized RFID signal.')
                red_neon_led()
                time.sleep(2)
                black_neon_led()
            





