#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from itertools import cycle

class App(Frame):
    def __init__(self, master, images, size, **args):
        Frame.__init__(self, master, **args)
        self.pos = 0
        self.size = size
        self.images = images
        self.make_widgets()
        self.pack(expand = YES, fill = BOTH)

    def make_widgets(self):
        width, height = self.size
        self.canvas = Canvas(self, bg = 'white', height = height, width = width)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = YES)
        Button(self, text = 'Next', command = self.on_next).pack(fill = X)
        Button(self, text = 'Prev', command = self.on_prev).pack(fill = X)
        Button(self, text = 'Quit', command = self.on_quit).pack(fill = X)

    def redraw(self):
        original = self.images[self.pos]
        self.image = ImageTk.PhotoImage(original.resize(self.size, Image.ANTIALIAS))
        self.canvas.delete("IMG")
        self.canvas.create_image(2, 2, image = self.image, anchor = NW, tags = "IMG")

    def on_next(self):
        self.pos = min(len(self.images) - 1, self.pos + 1)
        self.redraw()

    def on_prev(self):
        self.pos = max(0, self.pos - 1)
        self.redraw()

    def on_quit(self):
        self.update()
        self.quit()

    def run(self):
        self.redraw()
        self.mainloop()

if __name__ == "__main__":
    size = (1024, 768)
    root = Tk()
    images = [Image.open('tattoo.jpg'), Image.open('studio.jpg')]
    app = App(root, images = images, size = size, bd = 3, relief = SUNKEN)
    app.run()
