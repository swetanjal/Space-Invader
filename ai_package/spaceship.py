from ai import AI
import pygame
from font_package import *


class Spaceship(AI):
    def __init__(self, gameDisplay, x, y, width=100, height=75):
        AI.__init__(self, gameDisplay, x, y, width, height, colors.black)

    def draw(self):
        pygame.draw.polygon(self.display, self.color, [[(self.x + self.width / 2), self.y], [
                            self.x, self.y + self.height], [self.x + self.width, self.y + self.height]])
