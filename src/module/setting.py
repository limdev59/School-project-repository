#import json
from tkinter import Tk
import os
import json

tk = Tk()

path = __file__.replace('\setting.py','')
file_list = os.listdir(path)
print(path)
png_list = [file for file in file_list if file.endswith('.png')]
print(png_list)

json_list = [file for file in file_list if file.endswith('.json')]
print(json_list)

dict_list = []
for i in json_list:
    for line in open((path+'\\'+i),'r'):
        dict_list.append(json.loads(str(line)))
print(dict_list)

data = {
  "size" : [
    tk.winfo_screenwidth(),
    tk.winfo_screenheight()
  ],
  "shader": True
}

