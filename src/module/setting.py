#import json
from tkinter import Tk
import os
from module.Actor import *
import json

player_box = Box(100,100,64,64,32,48,0,0)



tk = Tk()

data = {
  "size" : [
    tk.winfo_screenwidth(),
    tk.winfo_screenheight()
  ],
  "shader": True
}

# path = __file__.replace('\setting.py','')
# file_list = os.listdir(path)
# print(path)
# png_list = [file for file in file_list if file.endswith('.png')]
# print(png_list)

# json_list = [file for file in file_list if file.endswith('.json')]
# print(json_list)

# dict_list = []
# for i in json_list:
#     for line in open((path+'\\'+i),'r'):
#         dict_list.append(json.loads(str(line)))
# print(dict_list)



