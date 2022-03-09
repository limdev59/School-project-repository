import json
from tkinter import *

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
with open("setting_data.json", "w") as json_file:
	json.dump(data, json_file)
	