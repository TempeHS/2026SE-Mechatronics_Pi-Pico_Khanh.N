from py_scripts.colorsensor import ColourSensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040


sensor = PiicoDev_VEML6040()
cs = ColourSensor(sensor, debug=True)

while True:
    rgb = cs.sensecolour()
    print(f'rgb: {rgb}')
