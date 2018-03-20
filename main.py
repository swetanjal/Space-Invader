import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
###################################################

#Implement inheritance of character
	
###################################################
class Spaceship():
	def __init__(self, gameDisplay, x, y, width=100, height=75):
		self.height=height
		self.width=width
		self.display=gameDisplay
		self.color=black
		self.x=x
		self.y=y
	def draw(self):
		pygame.draw.rect(self.display, self.color, [self.x , self.y , self.width , self.height])
###################################################
class Alien():
	def __init__(self, gameDisplay, x, y, death_time, width=100, height=75):
		self.height=height
		self.width=width
		self.display=gameDisplay
		self.color=red
		self.x=x
		self.y=y
		self.death_time=death_time
	def draw(self):
		pygame.draw.rect(self.display, self.color, [self.x , self.y , self.width , self.height])

###################################################

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

pygame.display.set_caption('Space Invader')

pygame.display.update()
gameExit = False
#Spaceship object
space_ship = Spaceship(gameDisplay, 0, 525)
timer = 0
aliens = []
aliens.append(Alien(gameDisplay, random.choice([0,100,200,300,400,500,600,700]), random.choice([1,0])*75, timer+(30*8)))
change = 0

while not gameExit:
	timer = timer+1
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				gameExit = True
			if event.key == pygame.K_d:
				change=10
			if event.key == pygame.K_a:
				change = -10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d or event.key == pygame.K_a:
				change=0
	if timer%300 == 0:
		aliens.append(Alien(gameDisplay, random.choice([0,100,200,300,400,500,600,700]), random.choice([1,0])*75, timer+(30*8)))
	for i in range(len(aliens)):
		if timer == aliens[i].death_time:
			aliens.pop(i)
	if change<0 and space_ship.x>-10:
		space_ship.x+=change
	if change>0 and space_ship.x<710:
		space_ship.x+=change
	gameDisplay.fill(white)
	space_ship.draw()
	for alien in aliens:
		alien.draw()
	pygame.display.update()
	clock.tick(30)
pygame.quit()
quit()