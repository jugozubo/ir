# main.py -- put your code here!
from machine import Pin
from time import sleep
from ir_rx.nec import NEC_8
led=Pin(4,Pin.OUT)
pin=Pin(13,Pin.IN)
recibo=0
def ir_callback(data,addr,clt):
    global recibo
    print("El codigo recibido es ",hex(data))
    recibo=hex(data)
ir=NEC_8(pin,ir_callback)
print("Esperando señal del control")
while True:
    if recibo!='-0x1':
        if recibo=='0x11':
            led.on()
        if recibo=='0x12':
            led.off()
        sleep(0.5)