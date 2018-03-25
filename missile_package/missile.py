import pygame


class Missile(object):
    def __init__(self, gameDisplay, x, y, birth_time, width, height, sprite):
        x = x + 36
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.display = gameDisplay
        self.img = pygame.image.load(sprite)
        self.birth_time = birth_time

    def draw(self):
        self.display.blit(self.img, (self.x, self.y))
