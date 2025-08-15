from machine import Pin, PWM
from servo import Servo
# my_servo = left    my_servo2 = right

class ServoMove:
    def __init__(self, my_servo, my_servo2):
        self.my_servo = my_servo
        self.my_servo2 = my_servo2

    def moveforward(self):
        self.my_servo.set_duty(500)
        self.my_servo2.set_duty(2500)