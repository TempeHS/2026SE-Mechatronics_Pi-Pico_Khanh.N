from machine import Pin, PWM
from servo import Servo

# Initialize servo instances
l_servo = Servo(PWM(Pin(16)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
r_servo = Servo(PWM(Pin(15)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

class ServoMovement:
    def __init__(self, l_servo, r_servo, forward, left, right, reverse, stop):
        self.l_servo = l_servo
        self.r_servo = r_servo
        self._forward = forward
        self._left = left
        self._right = right
        self._reverse = reverse
        self._stop = stop

    def move_forward(self):
        self.l_servo.set_duty(self._forward[0])
        self.r_servo.set_duty(self._forward[1])

    def turn_left(self):
        self.l_servo.set_duty(self._left[0])
        self.r_servo.set_duty(self._left[1])

    def turn_right(self):
        self.l_servo.set_duty(self._right[0])
        self.r_servo.set_duty(self._right[1])

    def move_reverse(self):
        self.l_servo.set_duty(self._reverse[0])
        self.r_servo.set_duty(self._reverse[1])

    def stop_movement(self):
        self.l_servo.set_duty(self._stop[0])
        self.r_servo.set_duty(self._stop[1])

# Example duty values (adjust based on your servo calibration)
forward = (1600, 1400)
left = (1500, 1400)
right = (1600, 1500)
reverse = (1400, 1600)
stop = (1500, 1500)

# Create movement controller
movement = ServoMovement(l_servo, r_servo, forward, left, right, reverse, stop)

# Example usage
movement.move_forward()
