import sys, pygame
import screen_setting as sc
from tkinter import *
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((100,100))
clock = pygame.time.Clock(sc.data["clock"]) 

while True:
	for event in pygame.event.get():
	  if event.type == QUIT:
	  	pygame.quit()
	  	sys.exit()
	pygame.display.update()
