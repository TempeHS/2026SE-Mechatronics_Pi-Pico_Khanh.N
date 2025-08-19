from colorsensor import Colour_Sensor

sensor = Colour_Sensor(debug=False)

while True: 
    result = sensor.check_colour()
    print(result)
    sleep(0.5)