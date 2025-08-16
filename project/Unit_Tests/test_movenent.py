# Updated Movement Test for Pi Pico Robot
from time import sleep

# Import your movement object from movement.py
from movement import movement

print("Starting updated movement sequence...")
sleep(2)

# Forward for 5 seconds (both wheels forward)
print("Moving forward for 5 seconds...")
movement.move_forward()
sleep(5)

# Turn right for 2 seconds
print("Turning right for 2 seconds...")
movement.turn_right()
sleep(2)

# Turn left for 2 seconds
print("Turning left for 2 seconds...")
movement.turn_left()
sleep(2)

# Backward for 4 seconds (both wheels backward)
print("Moving backward for 4 seconds...")
movement.move_backward()
sleep(4)

# Stop
print("Stopping...")
movement.stop()

print("Updated movement sequence complete!")