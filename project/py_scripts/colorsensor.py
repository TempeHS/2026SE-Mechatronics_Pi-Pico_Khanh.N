class ColourSensor:
    def __init__(self, coloursensor, debug=False):
        self.__coloursensor = coloursensor
        self.__debug = debug

    def sensecolour(self):
        rgb = self.__coloursensor.readRGB()
        if self.__debug:
            print(rgb)
        return rgb