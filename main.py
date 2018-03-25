#Importing required packages
import pygame
import time
import random
from ai_package.spaceship import Spaceship
from ai_package.ai import AI
from ai_package.alien import Alien
from missile_package import Missile1
from missile_package import Missile2
from missile_package import Missile
from font_package import colors

def message_to_screen(msg, color=colors.red):
	"""This function is used to display some text on the screen"""
	font = pygame.font.SysFont(None, 75)
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [275,650])

def spawn_alien(aliens):
	"""This function is used to get the location of the new alien to be spawned. Care is taken
		that two aliens are not at the same location at any instant"""
	x = random.choice([0,100,200,300,400,500,600,700])
	y = random.choice([1,0])*75
	for alien in aliens:
		if alien.x==x and alien.y==y:
			return spawn_alien(aliens)
	return [x,y]

def missile_draw(missiles, rate):
	"""This function is used to update the location of missiles and redraw them on the window"""
	for missile in missiles:
		if (timer-missile.birth_time)>0 and (timer-missile.birth_time)%(30/rate) == 0:
			missile.y=missile.y - 75
		missile.draw()

def destroy_aliens(aliens):
	"""This function is used to destroy aliens whose lifetime has expired"""
	i=0
	while i < (len(aliens)):
		if timer == aliens[i].death_time:
			aliens.pop(i)
			i=i-1
		i=i+1

pygame.init()
gameDisplay = pygame.display.set_mode((800,700))
clock = pygame.time.Clock()

pygame.display.set_caption('Space Invader')

pygame.display.update()
gameExit = False
space_ship = Spaceship(gameDisplay, 0, 525)
timer = 0
change = 0
score=0
aliens = []
missiles1 = []
missiles2 = []

x , y = spawn_alien(aliens)
aliens.append(Alien(gameDisplay, x, y, timer+(30*8)))	

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
		x , y = spawn_alien(aliens)
		aliens.append(Alien(gameDisplay, x, y, timer+(30*8)))
	destroy_aliens(aliens)
	gameDisplay.fill(colors.white)
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
				aliens[j].color=colors.yellow
				missiles2.pop(i)
				i=i-1
				break
			j=j+1
		i=i+1
	message_to_screen("SCORE: "+str(score))
	for alien in aliens:
		alien.draw()
	missile_draw(missiles1, 1)
	missile_draw(missiles2, 2)
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