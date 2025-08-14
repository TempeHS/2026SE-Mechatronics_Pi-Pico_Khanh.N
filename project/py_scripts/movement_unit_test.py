from machine import Pin, PWM
from servo import Servo
from Movement import ServoMovement
from time import sleep

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)
right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

movement = ServoMovement(
    forward=(1600, 1400),
    left=(1400, 1400),
    right=(1600, 1600),
    reverse=(1400, 1600),
    stop=(1500, 1500)
)

print("test forward")
movement.forward()
sleep(2)

print("test left turn")
movement.left()
sleep(1)

print("test reverse")
movement.reverse()
sleep(2)

print("test stop")
movement.stop()
sleep(1)

print("unit test ")