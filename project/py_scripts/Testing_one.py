from servomove import ServoMove
from time import sleep_ms
from machine import Pin, PWM  


left_servo = PWM(Pin(16))   # Replace with actual pin number
right_servo = PWM(Pin(15))  # Replace with actual pin number


left_servo.freq(50)
right_servo.freq(50)


forward = (1600, 1400)
left = (1500, 1400)
right = (1600, 1500)
reverse = (1400, 1600)
stop = (1500, 1500)


movement = ServoMove(
    left_servo,
    right_servo,
    forward,
    left,
    right,
    reverse,
    stop
)

while True:
    movement.move_forward()
    sleep_ms(1000)

    movement.turn_left()
    sleep_ms(1000)

    movement.turn_right()
    sleep_ms(1000)

    movement.move_reverse()
    sleep_ms(1000)

    movement.stop_movement()
    sleep_ms(2000)
