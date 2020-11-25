import pygame
import time
import random
pygame.init()


def color(x , y , screen , color):
	pygame.draw.rect(screen , color  , (x , y , 20 , 20))

def main():
	running = True
	screen  = pygame.display.set_mode((820 , 620))
	snake = [[100 , 100] , [120 , 100] , [140 , 100]]
	food = [400 , 300]
	eaten = False
	score = 0
	vx = 0
	vy = 0
	while running:
		if eaten:
			food = [random.randint(2 , 7)*100 , random.randint(2 , 6)*100]
			score += 1
			eaten = False
		
		if snake[len(snake) - 1] == food:
			snake.insert(0 , [snake[0][0] - 20 , snake[0][1]])
			eaten = True
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					vx = 20
					vy = 0
				elif event.key == pygame.K_LEFT:
					vx = -20
					vy = 0
				elif event.key == pygame.K_DOWN:
					vy = 20
					vx = 0
				elif event.key == pygame.K_UP:
					vy = -20
					vx = 0
		length = len(snake)-1
		for i in range(len(snake) - 1):
			if snake[i] == snake[length]:
				print("game over!!!!")
				exit()
			
		screen.fill((30 , 30 , 30))
		for i in range(0 , 820 , 20):
			for j in range(0 , 620 , 20):
				pygame.draw.rect(screen , (100 , 100 , 100) , (i , j , 20 , 20) , 2)
		
		if vx != 0 or vy != 0:
			for i in range(len(snake)):
				if i == len(snake) - 1:
					if snake[i][0] <= 800 and snake[i][0] >= 0:
						snake[i][0] += vx
					elif snake[i][0] > 800:
						snake[i][0] = 0
					elif snake[i][0] < 0:
						snake[i][0] = 800
					
					if snake[i][1] <= 600 and snake[i][1] >= 0:
						snake[i][1] += vy
					elif snake[i][1] > 600:
						snake[i][1] = 0
					elif snake[i][1] < 0:
						snake[i][1] = 600
				else:
					snake[i][0] =  snake[i + 1][0]
					snake[i][1] = snake[i + 1][1]
		
		color(*food , screen , (100 , 0 , 0))
		
		for coord in snake:
			color(*coord , screen , (255 , 255 , 255))
		
		
		
		pygame.display.update()
		time.sleep(1/10)

main()