from time import sleep
from movement import movement

print("Starting updated movement sequence...")
sleep(2)

# Forward for 5 seconds (both wheels forward)
print("Moving forward for 5 seconds...")
movement.move_forward()
sleep(5)

