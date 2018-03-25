from missile import Missile

missile2_sprite = 'sprites/missile2.png'


class Missile2(Missile):
    def __init__(self, gameDisplay, x, y, birth_time, width=25, height=75):
        Missile.__init__(self, gameDisplay, x, y, birth_time,
                         width, height, missile2_sprite)
        self.x -= 15
