from ai import AI

alien_sprite = 'sprites/alien.png'


class Alien(AI):
    def __init__(self, gameDisplay, x, y, death_time, width=100, height=75):
        AI.__init__(self, gameDisplay, x, y, width, height, alien_sprite)
        self.death_time = death_time
