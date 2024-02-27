from .Tile import Tile
from .constants import *
import pygame
from .secret_screen import template as colors

def draw(win: pygame.Surface, grid: list):
    """Draws the grid and the spots"""
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw()
    
    pygame.display.update()

def get_pos(pos: tuple, rows: int, width: int):
    """Gets the position of the mouse click"""
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def make_grid(rows: int, width: int, root) -> list:
    """Creates a grid of spots"""
    import numpy as np
    grid = np.empty((rows, rows), dtype=object)
    gap = width // rows
    for i in range(rows):
        for j in range(rows):
            tile = Tile(i, j, gap, root)
            grid[i, j] = tile
    return list(grid)

def save(grid: list):
    """Saves the grid"""
    # Grid is two dimensional list of Tile objects and tile.color is a tuple
    # We will write a two dimensional list that contains the color of the tiles
    with open("secret_screen.py", "w") as file:
        file.write("template: list[list[tuple[int, int, int]]] = [\n")
        for i in range(len(grid)):
            file.write("[")
            for j in range(len(grid[i])):
                file.write(f"{grid[i][j].color}, ")
            file.write("],\n")
        file.write("]\n")

def load_grid(rows: int, width: int, root: pygame.Surface):
    """Loads the grid"""
    import numpy as np
    grid = np.empty((rows, rows), dtype=object)
    gap = width // rows
    for i in range(rows):
        for j in range(rows):
            tile = Tile(i, j, gap, root, colors[i][j])
            grid[i, j] = tile

    # print(list(grid))
    return list(grid)
