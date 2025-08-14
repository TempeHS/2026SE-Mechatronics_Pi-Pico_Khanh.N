from machine import Pin, PWM
from servo import Servo
from time import sleep

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)
right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

class ServoMovement:
    def __init__(self, forward, left, right, reverse, stop):
        self.__forward = forward
        self.__left = left
        self.__right = right
        self.__reverse = reverse
        self.__stop = stop

    def forward(self):
        left_servo.set_duty(self.__forward[0])#1600
        right_servo.set_duty(self.__forward[1])#1400
    
    def left(self):
        left_servo.set_duty(self.__left[0])#1400
        right_servo.set_duty(self.__left[1])#1400

    def right(self):
        left_servo.set_duty(self.__right[0])#1600
        right_servo.set_duty(self.__right[1])#1600

    def reverse(self):
        left_servo.set_duty(self.__reverse[0])#1400
        right_servo.set_duty(self.__reverse[1])#1600

    def stop(self):
        left_servo.set_duty(self.__stop[0])#1500
        right_servo.set_duty(self.__stop[1])#1500

# maybe delete ???
servo_moves = ServoMovement(
    forward=(1600, 1400),
    left=(1400, 1400),
    right=(1600, 1600),
    reverse=(1400, 1600),
    stop=(1500, 1500)
)
while True:
    servo_moves.forward()
    sleep(2)

    servo_moves.left()
    sleep(1)

    servo_moves.reverse()
    sleep(2)

    servo_moves.stop()
    #sleep(1)  ## can remove that so it just stop 

### if that doesnt work can put the values straight in