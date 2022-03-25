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
  
class Animation:
  def __init__(self,anims):
    self.anims = anims # Array
    self.anim_count = len(anims)
    present_image = anims
    return present_image
      

class Actor(object):
  def __init__(self,x,y,coll_x,coll_y):
    self.x = x
    self.y = y
    self.velocity = 0
    self.frame = self.is_stop
    self.is_stop = (self.velocity == 0)
    self.size = [1,1] # Size
    self.coll = [coll_x,coll_y] # Collision
    self.anims = 
    self.draw_image = Animation(anims)
  
  def draw(self, screen):
    if self.speed > 0:
      self.speed

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
  
  
  