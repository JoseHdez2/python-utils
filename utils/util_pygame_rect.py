import pygame
import util_color as UC

class MyRect(pygame.Rect):
    
    def __init__(self, pos, size, color):
        self.color = color
        super().__init__(pos, size)

def mk_rect(pos, dim, color=(0,255,255)):
    return MyRect(pos, dim, color)

def make_square(pos, dim, color):
    return mk_rect(pos, (dim, dim), color)

def make_grid(rows, cols, pps):
    rects = []
    for x in range(0,rows):
        for y in range(0,cols):
            sX = x * pps
            sY = y * pps
            rects.append(make_square((sX,sY), pps, UC.mutate_color(0,255,0,20)))
    return rects