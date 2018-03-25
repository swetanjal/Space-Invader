from ai import AI
import pygame
from font_package import *


class Alien(AI):
    def __init__(self, gameDisplay, x, y, death_time, width=100, height=75):
        AI.__init__(self, gameDisplay, x, y, width, height, colors.red)
        self.death_time = death_time

    def draw(self):
        pygame.draw.rect(self.display, self.color, [
                         self.x, self.y, self.width, self.height])
