#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from itertools import cycle

class App(Frame):
    def __init__(self, master, delay, images):
        Frame.__init__(self, master)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.delay = delay
        self.size = (master.winfo_width(), master.winfo_height())
        self.images = cycle(images)
        self.display = Canvas(self, bd = 0, highlightthickness = 0)
        self.display.grid(row = 0, sticky = W + E + N + S)
        self.pack(fill = BOTH, expand = 1)

    def next_slide(self):
        original = next(self.images)
        self.image = ImageTk.PhotoImage(original.resize(self.size, Image.ANTIALIAS))
        self.display.delete("IMG")
        self.display.create_image(0, 0, image = self.image, anchor = NW, tags = "IMG")
        self.after(self.delay, self.next_slide)

    def run(self):
        self.next_slide()
        self.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry('1024x768')
    root.update()
    images = [Image.open('tattoo.jpg')]
    app = App(root, 3000, images)
    app.run()
