#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from itertools import cycle

class App(Frame):
    def __init__(self, master, images, size, min_marks = 2, **args):
        Frame.__init__(self, master, **args)
        self.pos = 0
        self.size = size
        self.marked = set()
        self.min_marks = min_marks
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
        self.mark_button = Button(self, text = 'Mark', command = self.on_mark)
        self.mark_button.pack(fill = X)
        Button(self, text = 'Quit', command = self.on_quit).pack(fill = X, side = BOTTOM)

    def refresh_marks(self):
        at_least = max(0, self.min_marks - len(self.marked))
        self.mark_button.config(text = "Mark" if self.pos not in self.marked else "Unmark")
        self.label.config(text = "You marked %d images, mark at least %d more" % (len(self.marked), at_least))

    def refresh_picture(self):
        original = self.images[self.pos]
        self.image = ImageTk.PhotoImage(original.resize(self.size, Image.ANTIALIAS))
        self.canvas.delete("IMG")
        self.canvas.create_image(2, 2, image = self.image, anchor = NW, tags = "IMG")
        self.refresh_marks()

    def on_next(self):
        self.pos = min(len(self.images) - 1, self.pos + 1)
        self.refresh_picture()

    def on_prev(self):
        self.pos = max(0, self.pos - 1)
        self.refresh_picture()

    def on_mark(self):
        if self.pos not in self.marked:
            self.marked.add(self.pos)
        else:
            self.marked.remove(self.pos)
        self.refresh_marks()

    def on_quit(self):
        self.update()
        self.quit()

    def run(self):
        self.refresh_picture()
        self.mainloop()

if __name__ == "__main__":
    size = (1024, 768)
    root = Tk()
    root.title('Tattoo Coloring')
    images = [Image.open('tattoo.jpg'), Image.open('studio.jpg')]
    app = App(root, images = images, size = size, bd = 3, relief = SUNKEN)
    app.run()
