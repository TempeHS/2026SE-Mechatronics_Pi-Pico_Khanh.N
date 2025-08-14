from machine import Pin, PWM
from servo import Servo
# my_servo = left    my_servo2 = right
my_servo = Servo(pwm=PWM(Pin(16)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
my_servo2 = Servo(pwm=PWM(Pin(15)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

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
        self.my_servo.set_duty(self._forward)
        self.my_servo2.set_duty(self._forward)
    def left(self):
        self.my_servo.set_duty(self._left)
        self.my_servo2.set_duty(self._left)
    def right(self):
        self.my_servo.set_duty(self._right)
        self.my_servo2.set_duty(self._right)
    def reverse(self):
        self.my_servo.set_duty(self._reverse)
        self.my_servo2.set_duty(self._reverse)
    def stop(self):
        self.my_servo.set_duty(self._stop)
        self.my_servo2.set_duty(self._stop)

forward = (1600, 1400)
left = (1500, 1400)
right = (1600, 1500)
reverse = (1400, 1600)
stop = (1500, 1500)