import pygame
import subprocess

def options():
	def drawRect(line, i):
		pygame.draw.rect(window, (colorOfBlocks[i]), (line['x'], line['y'], line['widht'], line['height']))
	def drawText(lineImage, lineText):
		window.blit(lineImage, (lineText['x'], lineText['y']))
	i = 0
	k = 0 
	colorOfBlocks = []
	pygame.init()
	window = pygame.display.set_mode((500, 500))

	pygame.display.set_caption("Snake")

	run = True
	rectColor = (47,79,79)
	easy = {'x': 150, 'y': 160, 'widht': 200, 'height': 60}
	medium = {'x': 150, 'y': 250, 'widht': 200, 'height': 60}
	hard = {'x': 150, 'y': 340, 'widht': 200, 'height': 60}

	activeKeys = [easy, medium, hard]

	# описание легкого уровня
	easyText = {"Text": "EASY", "x": 220, "y": 180, "fontSize": 36}
	easyFontSize = pygame.font.SysFont("None", easyText['fontSize'])
	easyFontColor = (69,139,0)
	easyImage = easyFontSize.render(easyText['Text'], 0, (easyFontColor))
	# конец описания

	# описание среднего уровня
	mediumText = {"Text": "MEDIUM", "x": 210, "y": 270, "fontSize": 36}
	mediumFontSize = pygame.font.SysFont("None", mediumText['fontSize'])
	mediumFontColor = (69,139,0)
	mediumImage = mediumFontSize.render(mediumText['Text'], 0, (mediumFontColor))
	# конец описания

	# описани тяжелого уровня
	hardText = {"Text": "HARD", "x": 220, "y": 360, "fontSize": 36}
	hardFontSize = pygame.font.SysFont("None", hardText['fontSize'])
	hardFontColor = (69,139,0)
	hardImage = hardFontSize.render(hardText['Text'], 0, (hardFontColor))
	# конец описания

	# описание заголовока
	caption = {"Text": "OPTIONS", "x": 170, "y": 60, "fontSize": 48}
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

		drawText(fontImage, caption)

		drawRect(easy, 0)
		drawText(easyImage, easyText)
		
		drawRect(medium, 1)
		drawText(mediumImage, mediumText)
		
		drawRect(hard, 2)
		drawText(hardImage, hardText)

		pygame.display.update()

	pygame.quit()

	if i == 2 and k == 1:
		sped = 80

	elif i == 1 and k == 1:
		sped = 100
	elif i == 0 and k == 1:
		sped = 120
	return sped
