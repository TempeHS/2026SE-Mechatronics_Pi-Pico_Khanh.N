from machine import Pin, PWM
from servo import Servo
from time import sleep

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500  # this is the stop 

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)
right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

class ServoMovement:
    def __init__(self, forward, left, right, reverse, stop):
        self.__forward = forward
        self.__left = left
        self.__right = right
        self.__reverse = reverse
        self.__stop = stop

    def move_forward(self):
        left_servo.set_duty(self.__forward)
        right_servo.set_duty(self.__reverse)

    def move_backward(self):
        left_servo.set_duty(self.__reverse)
        right_servo.set_duty(self.__forward)

    def turn_left(self):
        left_servo.set_duty(self.__reverse)
        right_servo.set_duty(self.__reverse)

    def turn_right(self):
        left_servo.set_duty(self.__forward)        
        right_servo.set_duty(self.__forward)    

    def stop(self):
        left_servo.set_duty(self.__stop)
        right_servo.set_duty(self.__stop)

movement = ServoMovement(
    forward=1600,   
    left=1300,     
    right=1700,     
    reverse=1400,   
    stop=1500      
)