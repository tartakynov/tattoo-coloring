#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from itertools import cycle

class App(Frame):
    def __init__(self, master, images, size, min_likes = 2, **args):
        Frame.__init__(self, master, **args)
        self.pos = 0
        self.size = size
        self.liked = set()
        self.min_likes = min_likes
        self.images = images
        self.make_widgets()
        self.pack(expand = YES, fill = BOTH)

    def make_widgets(self):
        width, height = self.size
        self.label = Label(self)
        self.label.pack()
        self.canvas = Canvas(self, bg = 'white', height = height, width = width)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = YES)
        Button(self, text = 'Next', command = self.on_next).pack(fill = X)
        Button(self, text = 'Prev', command = self.on_prev).pack(fill = X)
        self.like_button = Button(self, text = 'Like', command = self.on_like)
        self.like_button.pack(fill = X)
        Button(self, text = 'Quit', command = self.on_quit).pack(fill = X, side = BOTTOM)

    def refresh_likes(self):
        at_least = max(0, self.min_likes - len(self.liked))
        self.like_button.config(text = "Like" if self.pos not in self.liked else "Unlike")
        self.label.config(text = "Image %d. Like at least %d more" % (self.pos + 1, at_least))

    def refresh_picture(self):
        original = self.images[self.pos]
        self.image = ImageTk.PhotoImage(original.resize(self.size, Image.ANTIALIAS))
        self.canvas.delete("IMG")
        self.canvas.create_image(2, 2, image = self.image, anchor = NW, tags = "IMG")
        self.refresh_likes()

    def on_next(self):
        self.pos = min(len(self.images) - 1, self.pos + 1)
        self.refresh_picture()

    def on_prev(self):
        self.pos = max(0, self.pos - 1)
        self.refresh_picture()

    def on_like(self):
        if self.pos not in self.liked:
            self.liked.add(self.pos)
        else:
            self.liked.remove(self.pos)
        self.refresh_likes()

    def on_quit(self):
        self.update()
        self.quit()

    def run(self):
        self.refresh_picture()
        self.mainloop()

if __name__ == "__main__":
    size = (1024, 768)
    root = Tk()
    images = [Image.open('tattoo.jpg'), Image.open('studio.jpg')]
    app = App(root, images = images, size = size, bd = 3, relief = SUNKEN)
    app.run()
