from machine import Pin, PWM
from servo import Servo

my_servo = Servo(PWM=PWM(Pin(16)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
my_servo2 = Servo(pwm=PWM(Pin(15)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

class ServoMove:
    def __init__(self, my_servo, my_servo2, forward, left, right, reverse, stop):
        self.l_servo = my_servo
        self.r_servo = my_servo2
        self.__forward = forward
        self.__left = left
        self.__right = right
        self.__reverse = reverse
        self.__stop = stop

    def __-