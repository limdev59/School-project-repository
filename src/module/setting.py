#import json
from tkinter import Tk

tk = Tk()

data = {
  "size" : [
    tk.winfo_screenwidth(),
    tk.winfo_screenheight()
  ],
  "shader": True
}
	