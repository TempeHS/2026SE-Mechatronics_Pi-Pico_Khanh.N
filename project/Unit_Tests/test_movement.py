from time import sleep
from movement import movement

print("Starting updated movement sequence...")
sleep(2)

# Forward for 5 seconds (both wheels forward)
print("Moving forward for 5 seconds...")
movement.move_forward()
sleep(2)

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
sleep(2)

# Stop
print("Stopping...")
movement.stop()

print("Updated movement sequence complete!")