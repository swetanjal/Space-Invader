from ai import AI

spaceship_sprite = 'sprites/spaceship.png'


class Spaceship(AI):
    def __init__(self, gameDisplay, x, y, width=100, height=75):
        AI.__init__(self, gameDisplay, x, y, width, height, spaceship_sprite)
