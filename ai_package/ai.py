import pygame


class AI:
    def __init__(self, gameDisplay, x, y, width, height, sprite):
        self.height = height
        self.width = width
        self.display = gameDisplay
        self.x = x
        self.y = y
        self.img = pygame.image.load(sprite)

    def draw(self):
        self.display.blit(self.img, (self.x, self.y))
