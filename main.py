import pygame
import time
import random
from ai_package import *
from missile_package import *
from font_package import *
###################################################
#Care must be taken that two aliens are not spawned at the same place
###################################################

def message_to_screen(msg, color=colors.red):
	font = pygame.font.SysFont(None, 75)
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [275,650])

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
