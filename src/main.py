import sys
import pygame as pg
from module.setting import *
from module.Actor import *
from pygame.locals import *
import random
import math

def main():
  clock = pg.time.Clock()
  
  pg.init()
  screen = pg.display.set_mode(data["size"])
  pg.display.set_caption("game window")
  screen.fill((20, 0, 40))

  act = []
  act.append(Actor(screen,'a',100,100,64,64,32,48,0,0))
  act[0].draw()

  
  
  done = 0
  while not done:
      pg.display.update()
      for e in pg.event.get():
          if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
            done = 1
            break
      clock.tick(50)
  pg.quit()

if __name__ == "__main__":
    main()
