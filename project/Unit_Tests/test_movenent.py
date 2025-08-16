from time import sleep
from movement import movement

print("Starting simple movement test...")
sleep(2)

# Test forward
print("Moving forward...")
movement.move_forward()
sleep(2)

# Test stop
print("Stopping...")
movement.stop()
sleep(1)

# Test backward
print("Moving backward...")
movement.move_backward()
sleep(2)

# Test stop
print("Stopping...")
movement.stop()
sleep(1)

# Test left turn
print("Turning left...")
movement.turn_left()
sleep(1)

# Test stop
print("Stopping...")
movement.stop()
sleep(1)

# Test right turn
print("Turning right...")
movement.turn_right()
sleep(1)

# Test stop
print("Stopping...")
movement.stop()

print("Test complete!")