# Make a microsoft paint like application using python
import pygame as pg
from .helpers import *
from .constants import *

WIDTH, HEIGHT = 800, 800


class Tile:
    
    def __init__(self, row: int, col: int, width: int, root: pg.Surface, color = WHITE):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = color
        self.rect = (self.x, self.y, width, width)
        self.width = width


        self.root = root

    def get_pos(self):
        return self.row, self.col
    
    def fill(self):
        self.color = BLACK

    def reset(self):
        self.color = WHITE

    def green(self):
        self.color = GREEN

    def yellow(self):
        self.color = YELLOW

    def draw(self):
        pg.draw.rect(self.root, self.color, self.rect)

    def __deepcopy__(self, memo):
        return Tile(self.row, self.col, self.width, self.root, self.color)
