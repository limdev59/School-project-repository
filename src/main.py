import sys
import pygame as pg
from module.setting import *
from tkinter import *
from pg.locals import *

pg.init()
screen = Screen()
pg.display.set_mode(screen.monitor_size)
clock = pg.time.Clock(60)
while True:
	for event in pg.event.get():
	  if event.type == QUIT:
	  	pg.quit()
	  	sys.exit()
	pg.display.update()
