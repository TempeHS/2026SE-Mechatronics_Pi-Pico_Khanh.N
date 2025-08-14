from servomove import ServoMove
from time import sleep_ms
from machine import Pin, PWM 


movement = ServoMove(

)


forward = (1600, 1400)
left = (1500, 1400)
right = (1600, 1500)
reverse = (1400, 1600)
stop = (1500, 1500)