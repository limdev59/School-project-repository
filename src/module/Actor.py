import pygame
from enum import Enum

class Effects(Enum):
  slow = 1 # Slow
  poison = 2 # Damage that gets weaker
  weak = 3 # Decress atk
  fire_I = 4 # Default fire
  fire_II = 5 # Inferno
  freezing = 5
  curse_wave = 6 # It HUUUUUUUUUUUUUUUUUUURTS!!!!!!!
  deus_ex_machina = 7 # If Player get this effect, it will die in three hits
  regeneration = 8
  resistance = 9
  fire_inchant = 13
  freezing_inchant= 14
  curse_inchant= 15
  
# class Animation:
#   def __init__(self,anims):
#     self.anims = anims # Array
#     self.anim_count = len(anims)
#     present_image = anims
#     return present_image
      

class Actor(object):
  def __init__(self,screen,name=None,x=None,y=None,xsize=64,ysize=64,cx=32,cy=48,v=0,dir=0):
    self.screen = screen
    self.name = name
    self.x = x
    self.y = y
    self.velocity = v
    self.direction = dir # 0:RIGHT 1:UP 2:LEFT 3:DOWN
    self.frame = 0
    self.is_stop = (self.velocity == 0)
    self.size = [xsize,ysize] # Size
    self.coll = [cx,cy] # Collision
    self.anims = []
  
  def draw(self):
    if self.velocity > 0:
      self.screen.blit(self.anims[self.direction+self.frame],(self.x,self.y))
      self.frame += 1
      
  def setSize(self,x,y):
      self.size = [x,y]
      return self.size

  def getSize(self):
      return self.size

  def setColl(self,x,y):
      self.coll = [x,y]
      return self.coll

  def getColl(self):
      return self.coll

class Player(Actor):
  def __init__(self,screen,name=None,x=None,y=None,xsize=64,ysize=64,cx=32,cy=48,v=0,dir=0):
    self.screen = screen
    self.name = name
    self.x = x
    self.y = y
    self.velocity = v
    self.direction = dir
    self.frame = 0
    self.is_stop = (self.velocity == 0)
    self.size = [xsize,ysize]
    self.coll = [cx,cy]
    self.anims = []
  