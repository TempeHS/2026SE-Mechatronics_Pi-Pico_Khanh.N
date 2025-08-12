from led_light import Led_Light
from time import sleep

#set light 
led = Led_Light(3, False, True )

print('testing on()')
led.on()
if led.value() == 1:
    print('on() Passed')

sleep(.1)

print('testing off()')
led.off()
if led.value() == 0:
    print('off() passed')

print('testing toggle')
led.toggle()
if led.value() == 1:
    print('.toggle .on() passed')
sleep(1)
led.toggle()
sleep(1)
if led.value() == 0:
    print('.toggle .off() passed')