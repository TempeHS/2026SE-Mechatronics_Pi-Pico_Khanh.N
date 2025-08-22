# p14 : LED screen    
# p10 : color sensor   FINISH
# p30 : Ultrasonic sensor  might work ( cant really test since the base of the ultrasonic is broken)
#ultrasonic need to work. 
# detect green - stop for 2 seconds - keep going 
# led screen show the states of the robot eg. print forward when moving forward

from movement import movement
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from time import sleep


range_Front = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_Right = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
display = create_PiicoDev_SSD1306()
colorSensor = PiicoDev_VEML6040()

class Colour_Sensor:
    def __init__(self, debug):
        self.__debug = debug

    def check_colour(self):
        if self.__debug:
            print("Checking Colour")
        
        data = colorSensor.readHSV()
        hue = data['hue']
        
        if hue > 75 and hue < 85:
            return "green"
        else:
            return "not green"


color_sensor = Colour_Sensor(debug=False)

def make_turn(direction):
    movement.stop()
    
    
    display.fill(0)
    if direction == "right":
        display.text("TURNING", 20, 15, 1)
        display.text("RIGHT", 20, 30, 1)
        display.show()
        movement.turn_right()
    elif direction == "left":
        display.text("TURNING", 20, 15, 1)
        display.text("LEFT", 20, 30, 1)
        display.show()
        movement.turn_left()

    sleep(0.9) # this might the turn degree 
    movement.stop()
    sleep(0.1)

    display.fill(0)
    display.text("FORWARD", 20, 15, 1)
    display.text("AFTER TURN", 20, 30, 1)
    display.show()
    movement.move_forward()
    sleep(0.2)
    movement.stop()
    sleep(0.2)


display.fill(0)
display.text("STARTING", 20, 30, 1)
display.show()
sleep(1)

while True:

    front_distance = range_Front.distance_mm
    right_distance = range_Right.distance_mm

    if front_distance > 100:
    
        display.fill(0)
        display.text("MOVING", 20, 10, 1)
        display.text("FORWARD", 20, 25, 1)
        display.show()
        #sleep_ms(1000)

        movement.move_forward()
        
        
        color_result = color_sensor.check_colour()
        if color_result == "green":
            display.fill(0)
            display.text("GREEN", 20, 10, 1)
            display.text("STOPPING", 20, 40, 1)
            display.show()

            movement.stop()
            sleep(2)
            movement.move_forward()
            display.fill(0)
            display.text("FORWARD", 20, 30, 1)
            display.show()
            sleep(0.5)

        
    else:
        
        display.fill(0)
        display.text("OBSTACLE", 20, 10, 1)
        display.show()
        
        movement.stop()
        sleep(0.2)
        
        if right_distance > 100:
            
            display.fill(0)
            display.text("RIGHT", 20, 15, 1)
            display.text("CLEAR", 20, 30, 1)
            display.show()
            sleep_ms(500) #change this 500 
            make_turn("right")
        else:
            
            display.fill(0)
            display.text("BLOCKED", 20, 30, 1)
            display.show()
            sleep_ms(500) #change this 500
            make_turn("left")
        
    sleep(0.1)