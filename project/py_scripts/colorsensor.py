from PiicoDev_VEML6040 import PiicoDev_VEML6040

class Colour_Sensor:
    def __init__(self, debug):
        self.__debug = debug
        self.colorSensor = PiicoDev_VEML6040()

    def check_colour(self):
        if self.__debug:
            print("Checking Colour")

        data = self.colorSensor.readHSV()
        hue = data['hue']

        if 75 < hue < 85:
            return "green"
        else:
            return "not green"