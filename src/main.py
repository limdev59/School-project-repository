import sys 
import pygame
from pygame.locals import *
from . import *

pygame.init()

while True:
	for event in pygame.event.get():
	  if event.type == QUIT:
	  	pygame.quit()
	  	sys.exit()
	pygame.display.update()
  
