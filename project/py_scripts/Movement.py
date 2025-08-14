from machine import Pin, PWM
from servo import Servo
# my_servo = left    my_servo2 = right

class ServoMove:
    def __init__(self, my_servo, my_servo2, forward, left, right, reverse, stop):
        self.my_servo = my_servo
        self.my_servo2 = my_servo2
        self._forward = forward
        self._left = left
        self._right = right
        self._reverse = reverse
        self._stop = stop

    def moveforward(self):
        self.my_servo.set_duty(self._forward[0])
        self.my_servo2.set_duty(self._forward[1])

    def left(self):
        self.my_servo.set_duty(self._left[0])
        self.my_servo2.set_duty(self._left[1])

    def right(self):
        self.my_servo.set_duty(self._right[0])
        self.my_servo2.set_duty(self._right[1])

    def reverse(self):
        self.my_servo.set_duty(self._reverse[0])
        self.my_servo2.set_duty(self._reverse[1])

    def stop(self):
        self.my_servo.set_duty(self._stop[0])
        self.my_servo2.set_duty(self._stop[1])