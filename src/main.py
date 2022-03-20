import sys
import pygame as pg
from module.setting import data
from pygame.locals import *
import random
import math

def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode(data["size"])
    pg.display.set_caption("game window")
    screen.fill((20, 0, 40))
    
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
