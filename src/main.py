import sys, pygame
import screen_setting as sc
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(400,100)
clock = pygame.time.Clock(sc.data["clock"]) 

while True:
	for event in pygame.event.get():
	  if event.type == QUIT:
	  	pygame.quit()
	  	sys.exit()
	pygame.display.update()
  
