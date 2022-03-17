import json, pygame
from tkinter import *

'''
data = {
  "size": [
    monitor_height,
    monitor_width
  ],
  "shader": True
}
'''
class Screen:
  
  def __init__(self):
  	self.root = Tk()
  	self.monitor_size = [self.root.winfo_screenheight(), self.root.winfo_screenwidth()]
  	self.shader = True
  	self.data = {
  	  "size": self.monitor_size,
        "shader": True
      } 
  	
  def importSetting(self):
    with open("./data/setting_data.json", "r") as fs:
      return fs
    
  def exportOption(self):
    with open("./data/setting_data.json", "w") as fs:
      return json.dump(self.data, fs)

root = Tk()
mainloop()
	