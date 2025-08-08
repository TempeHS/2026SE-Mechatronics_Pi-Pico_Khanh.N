from machine import Pin, PWM, RTC
from servo import Servo
import time

# Create PWM servo controllers for both wheels
servo_pwm = PWM(Pin(16))  # Right wheel
servo_pwm2 = PWM(Pin(15)) # Left wheel
rtc = RTC()

# Servo parameters
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# Create servo objects
my_servo = Servo(pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)
my_servo2 = Servo(pwm=servo_pwm2, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# State machine setup
time_last_change = rtc.datetime()
machine_state = 1

# Define states: duration in seconds and servo pulse width
states = [
    {"duration": 3, "position": 500},   # Slow turn
    {"duration": 6, "position": 1000},  # Medium turn
    {"duration": 9, "position": 1500},  # Neutral (stop)
    {"duration": 12, "position": 2000}, # Fast turn
]

while True:
    time_now = rtc.datetime()

    if machine_state == 1:
        my_servo.set_duty(state_1_state)
        my_servo2.set_duty(state_1_state)  # ← Added
        if time_now[6] - time_last_change[6] >= state_1_time:
            machine_state = 2
            time_last_change = rtc.datetime()  # ← Also add this
    
    elif machine_state == 2:
        my_servo.set_duty(state_2_state)
        my_servo2.set_duty(state_2_state)  # ← Added
        if time_now[6] - time_last_change[6] >= state_2_time:
            machine_state = 3
            time_last_change = rtc.datetime()
    
    elif machine_state == 3:
        my_servo.set_duty(state_3_state)
        my_servo2.set_duty(state_3_state)  # ← Added
        if time_now[6] - time_last_change[6] >= state_3_time:
            machine_state = 4
            time_last_change = rtc.datetime()
    
    elif machine_state == 4:
        my_servo.set_duty(state_4_state)
        my_servo2.set_duty(state_4_state)  # ← Added
        if time_now[6] - time_last_change[6] >= state_4_time:
            time_last_change = rtc.datetime()
            machine_state = 1
