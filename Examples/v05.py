from time import sleep
from pedestrian_button import Pedestrian_Button

button = Pedestrian_Button(22, debug=True)

button_first = button.button_state
if button_first is False:
    print(".button_state passed")
else:
    print(".button_state failed")

sleep(.1)

print('press the button')
pressed = False
if button.button_state:
    pressed = True
else:
    print('fail')        
sleep(0.1)

if pressed:
    print(".button_state passed")
else:
    print(".button_state failed")

print("button_state setter test")
button.button_state = False
sleep(0.1)
if button.button_state is False:
    print(".button_state setter passed")
else:
    print(".button_state setter failed")

print("Test complete")