from font_package import *
from missile import Missile


class Missile2(Missile):
    def __init__(self, gameDisplay, x, y, birth_time, width=25, height=75):
        Missile.__init__(self, gameDisplay, x, y, birth_time,
                         width, height, colors.blue)
