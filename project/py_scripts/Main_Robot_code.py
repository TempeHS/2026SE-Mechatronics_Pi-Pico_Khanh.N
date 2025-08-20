# p14 : LED screen    
# p10 : color sensor   FINISH
# p30 : Ultrasonic sensor (only the right ultrasonic work)

from movement import movement
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from time import sleep

range_Front = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_Right = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

while True:
    front_distance = range_Front.distance_mm
    right_distance = range_Right.distance_mm

    if front_distance <= 100:
        print("Obstacle")
        movement.stop()
        sleep(0.2)
    
    while right_distance <= 100: #elif
        print("turn right")
        movement.turn_right()
        sleep(0.3)
        movement.stop()
        sleep(0.1)
    
        right_distance = range_Right.distance_mm

        print("right clear")

        front_distance = range_Front.distance_mm

        if front_distance <= 100:
            continue
    
    print("Clear")
    movement.move_forward()
    sleep(0.1)

