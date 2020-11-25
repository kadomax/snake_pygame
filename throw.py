import pygame
import random
import time
import math
pygame.init()



def main():
	screen = pygame.display.set_mode((800 , 600))
	running = True
	vx = 0
	vy = -0
	
	pos = [400 , 300]
	radius = 10
	
	ay = 20
	ax = 0
	
	t = 0
	dt = 0.1
	while running:
		#timestep acc calculations can also be done here
		t += dt
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		#throwing logic using mouse positions
		if pygame.mouse.get_pressed()[0]:
			mouseX , mouseY = pygame.mouse.get_pos()
			if mouseX == 0:
				mouseX = 0.0001
			angle =round (math.atan(mouseY / mouseX) , 2)
			if mouseX > pos[0]:
				vx = 200*(math.cos(angle))
			else:
				vx = -200*(math.cos(angle))
			if mouseY < pos[1]:
				vy = -200*(math.sin(angle))
			else:
				vy = 200*(math.sin(angle))
		
		screen.fill((0 , 0 , 0))
		
		#get new velocity from acceleration
		vx = round(vx + ax*dt , 2)
		vy = round(vy + ay*dt , 2)
		
		#get new position from velocity(X)
		pos[0] = round(pos[0]+ vx*dt , 2)
		
		#colliders
		if pos[0] > 800 - radius:
			pos[0] = 800 - radius
			vy *= 0.8
			vx *= -0.6
		if pos[0] < radius:
			pos[0] = radius
			vy *= 0.8 #friction
			vx *= -0.6
		
		#get new position from velocity(Y)
		pos[1] =round(pos[1]  + vy*dt , 2 )
		
		#colliders
		if pos[1] > 600 - radius:
			pos[1] = 600 - radius
			vx *= 0.8 #friction
			vy *= -0.6
		if pos[1] < radius:
			pos[1] = radius
			vx *= 0.8 #friction
			vy  *= -0.6
		
		pygame.draw.circle(screen , (100 , 100 , 100) , [round(pos1[0]) ,round( pos1[1])] , radius)
			
			
			
			
			
		pygame.display.update()
		time.sleep(1/30)
	pygame.quit()

main()