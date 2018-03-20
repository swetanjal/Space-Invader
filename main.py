import pygame
import time

black = (0,0,0)
white = (255,255,255)
###################################################
class Spaceship():
	def __init__(self, gameDisplay, x, y, width=100, height=75):
		pygame.draw.rect(gameDisplay, black, [x , y , width , height])
###################################################


pygame.init()
gameDisplay = pygame.display.set_mode((800,600))


pygame.display.set_caption('Space Invader')

#move horizontally by 100
pygame.display.update()
gameExit = False
row_ship = 525
col_ship = 0
while not gameExit:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				gameExit = True
	gameDisplay.fill(white)
	sp=Spaceship(gameDisplay, col_ship, row_ship)
	#pygame.draw.rect(gameDisplay, black, [400,400,100,100])
	pygame.display.update()

pygame.quit()
quit()