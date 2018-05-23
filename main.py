import pygame
import subprocess
import pygame
import random
import os

i = 0
k = 0 
sped = 100
def main(sped):
	i = 0
	colorOfBlocks = []
	pygame.init()
	window = pygame.display.set_mode((500, 500))

	pygame.display.set_caption("Snake")

	run = True
	rectColor = (47,79,79)
	start = {'x': 150, 'y': 160, 'widht': 200, 'height': 60}
	options = {'x': 150, 'y': 250, 'widht': 200, 'height': 60}
	exit = {'x': 150, 'y': 340, 'widht': 200, 'height': 60}

	activeKeys = [start, options, exit]

	# описание старта
	startText = {"Text": "START", "x": 215, "y": 180, "fontSize": 36}
	startFontSize = pygame.font.SysFont("None", startText['fontSize'])
	startFontColor = (69,139,0)
	startImage = startFontSize.render(startText['Text'], 0, (startFontColor))
	# конец описания

	# описание опций
	optionsText = {"Text": "OPTIONS", "x": 200, "y": 270, "fontSize": 36}
	optionsFontSize = pygame.font.SysFont("None", optionsText['fontSize'])
	optionsFontColor = (69,139,0)
	optionsImage = optionsFontSize.render(optionsText['Text'], 0, (optionsFontColor))
	# конец описания

	# описани выхода
	exitText = {"Text": "EXIT", "x": 220, "y": 360, "fontSize": 36}
	exitFontSize = pygame.font.SysFont("None", exitText['fontSize'])
	exitFontColor = (69,139,0)
	exitImage = exitFontSize.render(exitText['Text'], 0, (exitFontColor))
	# конец описания

	# описание заголовока
	caption = {"Text": "Python SNAKE", "x": 130, "y": 60, "fontSize": 48}
	myFont = pygame.font.SysFont("None", caption['fontSize'])
	captionFontColor = (69,139,0)
	fontImage = myFont.render(caption["Text"], 0, (captionFontColor))
	# конец описания


	for x in range(0,len(activeKeys)):
		colorOfBlocks.append(rectColor)

	while run:
		pygame.time.delay(140)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_DOWN]:
			if i + 1 == len(activeKeys) :
				i = 0
			else:
				i += 1
		if keys[pygame.K_UP]:
			if i == 0:
				i = len(activeKeys) - 1
			else:
				i -=1

		if keys[pygame.K_RETURN]:
			run = False
			k = 1

		if keys[pygame.K_KP_ENTER]:
			run = False
			k = 1

		for x in range(0,len(activeKeys)):
			colorOfBlocks[x] = rectColor
			if i == x:
				colorOfBlocks[x] = (148,0,211)

		window.blit(fontImage, (caption['x'], caption['y']))

		pygame.draw.rect(window, (colorOfBlocks[0]), (start['x'], start['y'], start['widht'], start['height']))
		window.blit(startImage, (startText['x'], startText['y']))

		pygame.draw.rect(window, (colorOfBlocks[1]), (options['x'], options['y'], options['widht'], options['height']))
		window.blit(optionsImage, (optionsText['x'], optionsText['y']))

		pygame.draw.rect(window, (colorOfBlocks[2]), (exit['x'], exit['y'], exit['widht'], exit['height']))
		window.blit(exitImage, (exitText['x'], exitText['y']))

		pygame.display.update()

	pygame.quit()

	if i == 2:
		print("Good bye!!")
	elif i == 1 and k == 1:
		from options import options
		sped = options()
		main(sped)
	elif i == 0 and k == 1:
		from snake import snake
		snake(sped)
		main(sped)
main(sped)


