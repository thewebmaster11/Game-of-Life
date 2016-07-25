#!/usr/bin/env python
from Tkinter import *
world = []
pause = False
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.alive = False
    def update(self):
        around = 0
        for cell in world:
            if cell.x in [self.x+1,self.x-1] and cell.y == self.y and cell.alive:
                around += 1
            if cell.x == self.x and cell.y in [self.y+1,self.y-1] and cell.alive:
                around += 1
        if around in [0,1,4]:
            self.alive = False
        if around == 3:
            self.alive = True
def create(width,height):
    global world
    for x in range(width):
        for y in range(height):
            world += [Cell(x,y)]
def update():
    global world
    if not pause:
        for cell in world:
            cell.update()
    for cell in world:
        if cell.alive:
            canvas.create_rectangle(cell.x,cell.y,cell.x+20,cell.y+20,fill='#000000')
        if not cell.alive:
            canvas.create_rectangle(cell.x,cell.y,cell.x+20,cell.y+20,fill='#FFFFFF')
def clickevent(event):
    global world
    x = event.x / 20
    y = event.y / 20
    for cell in world:
        if cell.x == x and cell.y == y:
            cell.alive = not cell.alive
def pressSpace(event):
    global pause
    pause = not pause
window = Tk(screenName='Game of Life')
canvas = Canvas(window,width=200,height=200)
canvas.bind('<Button-1>',clickevent)
canvas.bind('<space>',pressSpace)
canvas.pack()
create(20,20)
master.after(1,update)
mainloop()
