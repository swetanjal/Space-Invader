from missile import Missile

missile1_sprite = 'sprites/missile1.png'


class Missile1(Missile):
    def __init__(self, gameDisplay, x, y, birth_time, width=25, height=75):
        Missile.__init__(self, gameDisplay, x, y, birth_time,
                         width, height, missile1_sprite)
