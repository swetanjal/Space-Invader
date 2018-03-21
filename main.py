import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)

###################################################
#Each rectangle in the grid is 100 X 75
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
		pygame.draw.polygon(self.display, self.color, [[(self.x+self.width/2),self.y], [self.x,self.y+self.height], [self.x+self.width,self.y+self.height]])
		#pygame.draw.rect(self.display, self.color, [self.x , self.y , self.width , self.height])
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
	def __init__(self, gameDisplay, x, y, birth_time, width=25, height=75):
		x=x+36
		self.height=height
		self.width=width
		self.x=x
		self.y=y
		self.display=gameDisplay
		self.color = black
		self.birth_time = birth_time
	def draw(self):
		pygame.draw.rect(self.display, self.color, [self.x , self.y , self.width , self.height])

class Missile2:
	def __init__(self, gameDisplay, x, y, birth_time, width=25, height=75):
		x=x+36
		self.height=height
		self.width=width
		self.x=x
		self.y=y
		self.display=gameDisplay
		self.color = blue
		self.birth_time = birth_time
	def draw(self):
		pygame.draw.rect(self.display, self.color, [self.x , self.y , self.width , self.height])	

def message_to_screen(msg, color=red):
	font = pygame.font.SysFont(None, 75)
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [275,650])
###################################################
pygame.init()
gameDisplay = pygame.display.set_mode((800,700))
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
				change=100
				if space_ship.x<700:
					space_ship.x+=change
				change=0			
			if event.key == pygame.K_a:
				change=-100
				if space_ship.x>0:
					space_ship.x+=change
				change=0			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				missiles1.append(Missile1(gameDisplay, space_ship.x, space_ship.y-75, timer))
			if event.key == pygame.K_s:
				missiles2.append(Missile2(gameDisplay, space_ship.x, space_ship.y-75, timer))
	if timer%300 == 0:
		aliens.append(Alien(gameDisplay, random.choice([0,100,200,300,400,500,600,700]), random.choice([1,0])*75, timer+(30*8)))
	i=0
	while i < (len(aliens)):
		if timer == aliens[i].death_time:
			aliens.pop(i)
			i=i-1
		i=i+1
	gameDisplay.fill(white)
	space_ship.draw()
	i=0
	while i<len(missiles1):
		j=0
		while j<len(aliens):
			if aliens[j].x<missiles1[i].x+missiles1[i].width and missiles1[i].x<aliens[j].x+aliens[j].width and aliens[j].y == missiles1[i].y:
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
			if aliens[j].x<missiles2[i].x+missiles2[i].width and missiles2[i].x<aliens[j].x+aliens[j].width and aliens[j].y == missiles2[i].y:
				aliens[j].death_time=timer+(5*30)
				aliens[j].color=yellow
				missiles2.pop(i)
				i=i-1
				break
			j=j+1
		i=i+1
	message_to_screen("SCORE: "+str(score))
	for alien in aliens:
		alien.draw()
	for missile in missiles1:
		if (timer-missile.birth_time)>0 and (timer-missile.birth_time)%30 == 0:
			missile.y=missile.y - 75
		missile.draw()
	for missile in missiles2:
		if (timer-missile.birth_time)>0 and (timer-missile.birth_time)%15 == 0:
			missile.y=missile.y - 75
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