import sys 
import pygame
from pygame.locals import *
from . import *

pygame.init()
screen = pygame.display.set_mode((0,0))
clock = pygame.time.Clock() 

while True:
	for event in pygame.event.get():
	  if event.type == QUIT:
	  	pygame.quit()
	  	sys.exit()
	pygame.display.update()
  
