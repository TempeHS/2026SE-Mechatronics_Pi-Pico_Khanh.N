"""
Sample code for servo library, demonstrating instantiation
and setting angles for a continuous servo the resulting wheel speed
of a set_duty(x) call are:

| Set duty |  Speed  | Direction |
| -------- | ------- | --------- |
|   500    | Fast    | Backward  |
|   1400   | Slow    | Backward  |
|   1500   | Stopped | None      |
|   1600   | Slow    | Forward   |
|   2500   | Fast    | Forward   |

"""

import time
from machine import Pin, PWM
from servo import Servo


# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(15))

# create a servo object
my_servo = Servo(pwm=servo_pwm)
my_servo2 = Servo(pwm=servo_pwm2)

while True:
    # manually set the servo duty time
    my_servo.set_duty(500)
    my_servo2.set_duty(2500)
    time.sleep(2)

    my_servo.set_duty(1500)
    my_servo2.set_duty(1500)
    time.sleep(2)

    my_servo.set_duty(2500)
    my_servo2.set_duty(500)
    time.sleep(2)

    my_servo.stop()
    my_servo2.stop()
    time.sleep(2)
