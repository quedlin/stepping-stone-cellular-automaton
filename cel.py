# The Stepping Stone Cellular Automaton
# https://softologyblog.wordpress.com/2018/01/04/the-stepping-stone-cellular-automaton/

import pygame
import sys
import random

screen_width = 600
screen_height = 400
# NEIGHBOR_TYPE values:
# 1: 4 N,S,E,W Von-Neumann neighbors or 
# 2: all 8 closest cells in the Moore neighborhood
NEIGHBOR_TYPE = 1


pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()


bufferImage = pygame.Surface((screen_width, screen_height))
tmpImage = pygame.Surface((screen_width, screen_height))


image1 = pygame.image.load("pic1.png").convert()
bufferImage.blit(image1, (0,0))
tmpImage.blit(image1, (0,0))


UPDATEEVENT = pygame.USEREVENT+1
pygame.time.set_timer(UPDATEEVENT, 1000)

loop = True
press = False
while loop:
	try:
		#pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
				sys.exit()
			if event.type == UPDATEEVENT:

				pxarray = pygame.PixelArray(bufferImage)
				pxarraytmp = pygame.PixelArray(tmpImage)

				try:
					for y in range(1,screen_height-1):
						for x in range(1,screen_width-1):

							if random.randint(0,1) == 1:
								n = random.randint(1,4)
								if NEIGHBOR_TYPE == 1:									
									if n == 1:
										pxarraytmp[x, y] = pxarray[x, y-1]
									if n == 2:
										pxarraytmp[x, y] = pxarray[x-1, y]
									if n == 3:
										pxarraytmp[x, y] = pxarray[x+1, y]
									if n == 4:
										pxarraytmp[x, y] = pxarray[x, y+1]									
								if NEIGHBOR_TYPE == 2:
									if n == 1:
										pxarraytmp[x, y] = pxarray[x-1, y-1]
									if n == 2:
										pxarraytmp[x, y] = pxarray[x, y-1]
									if n == 3:
										pxarraytmp[x, y] = pxarray[x+1, y-1]
									if n == 4:
										pxarraytmp[x, y] = pxarray[x-1, y]
									if n == 5:
										pxarraytmp[x, y] = pxarray[x+1, y]
									if n == 6:
										pxarraytmp[x, y] = pxarray[x-1, y+1]
									if n == 7:
										pxarraytmp[x, y] = pxarray[x, y+1]
									if n == 8:
										pxarraytmp[x, y] = pxarray[x+1, y+1]

				except:
					print("Exception in update")
					loop = False
					sys.exit()

				bufferImage = tmpImage.copy()

		#px, py = pygame.mouse.get_pos()
		#if pygame.mouse.get_pressed() == (1,0,0):
		#	drawing with mouse
		#	bufferImage.set_at((px, py),(0, 255, 0))

		if event.type == pygame.MOUSEBUTTONUP:
			press == False

		screen.blit(bufferImage, (0, 0))
		pygame.display.flip()
		pygame.display.update()

		clock.tick(30)
	except Exception as e:
		print(e)		
		pygame.quit()

pygame.quit()