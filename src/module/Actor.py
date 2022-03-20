class Actor():
  def __init__(self):
    self.size = [1,1] # Size
    self.coll = [1,1] # Collision

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