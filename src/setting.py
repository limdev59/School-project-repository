import json
from tkinter import *

class screen:
  def getSetting(a,b):
    with open("./data/setting_data.json", "r") as json_file:
      
    
  def addSetting(a,b):
    with open("./data/setting_data.json", "w") as json_file:
      return json.dump(data, json_file) 
    
'''
root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))

data = {
  "size": [
    monitor_height,
    monitor_width
  ],
  "shader": "True"
  ]
}
mainloop()
'''
	