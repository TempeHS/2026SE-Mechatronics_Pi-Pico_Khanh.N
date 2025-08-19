from PiicoDev_VEML6040 import PiicoDev_VEML6040

colorSensor = PiicoDev_VEML6040()

class Colour_Sensor:
    def __init__(self, debug):
        self.__debug = debug

    def check_colour(self):
        if self.__debug:
            print("Checking Coulur")

        data = colorSensor.readHSV()
        hue = data['hue']

        if hue > 75 and hue < 85:
            return "green"
        else:
            return "not green"