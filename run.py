#!/usr/bin/env python

from Tkinter import *
from PIL import ImageTk, Image
import os

if __name__ == "__main__":
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("tattoo.jpg"))
    imglabel = Label(root, image = img).grid(row = 1, column = 1)
    root.mainloop()
