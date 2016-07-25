#!/usr/bin/env python
world
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
