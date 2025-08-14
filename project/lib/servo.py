try:
    from machine import Pin, PWM
except ImportError:
    class Pin:
        IN = 0
        PULL_UP = 0
        def __init__(self, pin, *a, **kw): pass
        def irq(self, *a, **kw): pass

    class PWM:
        def __init__(self, pin): pass
        def freq(self, f): pass
        def duty_ns(self, ns): pass
        def deinit(self): pass

try:
    from servo import Servo
except ImportError:
    class Servo:
        def __init__(self, *a, **kw): pass
        def set_duty(self, v): print(f"Servo set_duty({v})")


class Servo:
    """Servo class for pulse density modulation servos"""

    def __init__(
        self,
        pwm: PWM,
        min_us=500,
        max_us=2500,
        dead_zone_us=1500,
        freq=50,
    ):
        self.pwm = pwm
        self.pwm.freq(freq)
        self._move_period_ms = 1000 // freq
        min_us = min_us if min_us > 0 else 0
        max_us = max_us if min_us < max_us < (1000 // freq) * 1000 else 0
        self._curr_duty = 0
        self.dead_zone_us = dead_zone_us

    def set_duty(self, duty_us: int):
        self._curr_duty = duty_us
        self.pwm.duty_ns(duty_us * 1000)

    def set_angle(self, angle: int):
        angle = min(max(angle, 0), 180)
        duty_us = int(500 + (angle / 180) * 2000)
        self.set_duty(duty_us)

    def get_duty(self) -> int:
        return self._curr_duty

    def stop(self):
        self.set_duty(self.dead_zone_us)

    def deinit(self):
        self.pwm.deinit()
