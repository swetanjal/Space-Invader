import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
###################################################

#Implement inheritance of character
#Care must be taken that two aliens are not spawned at the same place
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
class Missile1:
	def __init__(self, gameDisplay, x, y, width=100, height=75):
		self.height=height
		self.width=width
		self.x=x
		self.y=y
		self.display=gameDisplay
		self.color = black
		self.speed = -2.5
	def draw(self):
		pygame.draw.rect(self.display, self.color, [self.x , self.y , self.width , self.height])

class Missile2:
	def __init__(self, gameDisplay, x, y, width=100, height=75):
		self.height=height
		self.width=width
		self.x=x
		self.y=y
		self.display=gameDisplay
		self.color = blue
		self.speed = -5.0
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
missiles1 = []
missiles2 = []
change = 0
score=0
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
			if event.key == pygame.K_SPACE:
				missiles1.append(Missile1(gameDisplay, space_ship.x, space_ship.y-75))
			if event.key == pygame.K_s:
				missiles2.append(Missile2(gameDisplay, space_ship.x, space_ship.y-75))
	if timer%300 == 0:
		aliens.append(Alien(gameDisplay, random.choice([0,100,200,300,400,500,600,700]), random.choice([1,0])*75, timer+(30*8)))
	i=0
	while i < (len(aliens)):
		if timer == aliens[i].death_time:
			if aliens[i].color == yellow:
				score+=1
			aliens.pop(i)
			i=i-1
		i=i+1
	if change<0 and space_ship.x>-10:
		space_ship.x+=change
	if change>0 and space_ship.x<710:
		space_ship.x+=change
	gameDisplay.fill(white)
	space_ship.draw()
	i=0
	while i<len(missiles1):
		j=0
		while j<len(aliens):
			if aliens[j].x<missiles1[i].x+missiles1[i].width and missiles1[i].x<aliens[j].x+aliens[j].width and aliens[j].y < missiles1[i].y and missiles1[i].y<aliens[j].y+aliens[j].height:
				score+=1
				aliens.pop(j)
				j=j-1
				missiles1.pop(i)
				i=i-1
				break
			j=j+1
		i=i+1
	i=0
	while i<len(missiles2):
		j=0
		while j<len(aliens):
			if aliens[j].x<missiles2[i].x+missiles2[i].width and missiles2[i].x<aliens[j].x+aliens[j].width and aliens[j].y < missiles2[i].y and missiles2[i].y<aliens[j].y+aliens[j].height:
				aliens[j].death_time=timer+(5*30)
				aliens[j].color=yellow
				missiles2.pop(i)
				i=i-1
				break
			j=j+1
		i=i+1
	print (score)
	for alien in aliens:
		alien.draw()
	for missile in missiles1:
		missile.y+=missile.speed
		missile.draw()
	for missile in missiles2:
		missile.y+=missile.speed
		missile.draw()
	i=0
	while i < (len(missiles1)):
		if missiles1[i].y<-100:
			missiles1.pop(i)
			i=i-1
		i=i+1
	i=0
	while i < (len(missiles2)):
		if missiles2[i].y<-100:
			missiles2.pop(i)
			i=i-1
		i=i+1
	pygame.display.update()
	clock.tick(30)
pygame.quit()
quit()