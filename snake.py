import pygame
import random
import os
import subprocess







def snake(sped):
	res = []
	def addBlock(coordinate):

		lenthOfSnake = len(coordinate) - 1

			
		if coordinate[lenthOfSnake][0] == coordinate[lenthOfSnake - 1][0]: # движение тела по вертикали
			if coordinate[lenthOfSnake][1] < coordinate[lenthOfSnake - 1][1]: # движение вниз
				coordinate.append([coordinate[lenthOfSnake][0],coordinate[lenthOfSnake][1] - 10])
			else: # движение вверх
				coordinate.append([coordinate[lenthOfSnake][0],coordinate[lenthOfSnake][1] + 10])
		elif coordinate[lenthOfSnake][1] == coordinate[lenthOfSnake - 1][1]: #движение по горизонтали
			if coordinate[lenthOfSnake][0] < coordinate[lenthOfSnake - 1][0]: # движение вправо
				coordinate.append([coordinate[lenthOfSnake][0] - 10,coordinate[lenthOfSnake][1]])
			else: # движение влево
				coordinate.append([coordinate[lenthOfSnake][0] + 10,coordinate[lenthOfSnake][1]])
		return coordinate

	def moveOfSnake(coordinate):
		lenthOfSnake = len(coordinate) - 1
		if lenthOfSnake == 0:
			return coordinate
		for x in range(lenthOfSnake,0,-1):
			coordinate[x][0] = coordinate[x-1][0]
			coordinate[x][1] = coordinate[x-1][1]
		return coordinate

	def newElemF(newElem):
		if newElem:
			newElemX = random.randrange(0,500,20)
			newElemY = random.randrange(0,500,20)
			if window.get_at((newElemX, newElemY)) != (0, 0, 0, 255):
				newElemF(newElem)
			newElem = False
		return [newElem, newElemX, newElemY]


	pygame.init()
	window = pygame.display.set_mode((500, 500))

	pygame.display.set_caption("Snake")

	coordinate = [[40,40]]
	x = coordinate[0][0]
	y = coordinate[0][1]
	widht = 10
	height = 10
	speed = 10


	counter = 0
	run = True
	newElem = True
	newElemX = 0
	newElemY = 0
	move = "x"

	while run :
		pygame.time.delay(sped)
		coordinate[0] = [x,y]
		if move == "-x": #left
			x -= speed
		if move == "x": #right
			x += speed
		if move == "y": #up
			y -= speed
		if move == "-y": #down
			y += speed
		coordinate = list(moveOfSnake(coordinate))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]  and move != "x":
			move = "-x"
		if keys[pygame.K_RIGHT] and move != "-x":
			move = "x"
		if keys[pygame.K_UP] and move != "-y":
			move = "y"
		if keys[pygame.K_DOWN] and move != "y":
			move = "-y"


		if (x == newElemX and y == newElemY) :
			coordinate = list(addBlock(coordinate))
			newElem = True
			counter += 10
		if newElem:
			res = newElemF(newElem)
			newElem = res[0]
			newElemX = res[1]
			newElemY = res[2]

		if x < 0 or x + widht > 500 or y < 0 or y + height > 500 :
			run = False
		else:
			if x != 0 and x != 500 and y != 0 and y != 500 and window.get_at((x, y)) == (0, 0, 255, 255):
				run = False

		window.fill((0,0,0))
		pygame.draw.rect(window, (61,89,171), (x, y, widht, height))

		if len(coordinate) > 1:
			for n in range(1,len(coordinate)):
				pygame.draw.rect(window, (0,0,255), (coordinate[n][0], coordinate[n][1], widht, height))
		pygame.draw.rect(window, (102,205,0), (newElemX, newElemY, widht, height))

		pygame.display.update()

	print(counter)
	pygame.quit()
	