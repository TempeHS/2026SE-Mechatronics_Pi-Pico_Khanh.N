import sys
import os

# Add the absolute path to the 'lib' directory
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib'))
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

# Add this at the top of Unit_Movement_test.py for Linux testing only
try:
    from machine import Pin, PWM
except ImportError:
    class Pin:
        IN = 0
        PULL_UP = 0
        def __init__(self, pin, *a, **kw): pass
        def irq(self, *a, **kw): pass

    class PWM:
        def __init__(self, pin): pass
        def freq(self, f): pass
        def duty_ns(self, ns): pass
        def deinit(self): pass

try:
    from servo import Servo
except ImportError:
    class Servo:
        def __init__(self, *a, **kw): pass
        def set_duty(self, v): print(f"Servo set_duty({v})")


from time import sleep
from servo import Servo

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
        self.my_servo.set_duty(500)
        self.my_servo2.set_duty(2500)

    def left(self):
        self.my_servo.set_duty(500)
        self.my_servo2.set_duty(2500)

    def right(self):
        self.my_servo.set_duty(500)
        self.my_servo2.set_duty(2500)

    def reverse(self):
        self.my_servo.set_duty(500)
        self.my_servo2.set_duty(2500)

    def stop(self):
        self.my_servo.set_duty(1500)
        self.my_servo2.set_duty(1500)

my_servo = Servo(PWM(Pin(16)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
my_servo2 = Servo(PWM(Pin(15)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

movement = ServoMove(
    my_servo2,
    my_servo,
    forward=(2500, 500),
    left=(1500, 500),
    right=(2500, 2500),
    reverse=(500, 2500),
    stop=(1500, 1500)
)

while True:
    movement.left()
    print(1)
    sleep(1)
    print(2)
    movement.stop()
    sleep(1)