import pygame


class Missile(object):
    def __init__(self, gameDisplay, x, y, birth_time, width, height, col):
        x = x + 36
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.display = gameDisplay
        self.color = col
        self.birth_time = birth_time

    def draw(self):
        pygame.draw.rect(self.display, self.color, [
                         self.x, self.y, self.width, self.height])
