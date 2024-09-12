from Assets import WIDTH, HEIGHT, make_grid, load_grid, draw, get_pos, save
from typing import TYPE_CHECKING
from copy import deepcopy
import pygame as pg
import sys

if TYPE_CHECKING:
    from Assets import Tile


ROOT = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pycrosoft Paint")


def main():
    ROWS = 100
    grid = make_grid(ROWS, HEIGHT, ROOT)

    run = True
    saved: list[Tile] = load_grid(ROWS, HEIGHT, ROOT)
    while run:
        draw(ROOT, grid)
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                run = False

            if pg.mouse.get_pressed()[0] and pg.mouse.get_pressed()[2]:
                pos = pg.mouse.get_pos()
                row, col = get_pos(pos, ROWS, HEIGHT)
                tile = grid[row][col]
                tile.yellow()

            elif pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                row, col = get_pos(pos, ROWS, HEIGHT)
                if row < 0 or col < 0:
                    continue
                tile = grid[row][col]
                tile.fill()

            elif pg.mouse.get_pressed()[2]:
                pos = pg.mouse.get_pos()
                row, col = get_pos(pos, ROWS, HEIGHT)
                tile = grid[row][col]
                tile.reset()

            elif pg.mouse.get_pressed()[1]:
                pos = pg.mouse.get_pos()
                row, col = get_pos(pos, ROWS, HEIGHT)
                tile = grid[row][col]
                tile.green()

            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_s:
                        print("Saving...")
                        saved = deepcopy(grid)
                        if any(arg for arg in sys.argv if arg == "-save"):
                            save(saved)

                    case pg.K_l:
                        grid = deepcopy(saved)
                        print("Loading...")

                    case pg.K_r:
                        grid = make_grid(ROWS, HEIGHT, ROOT)


if __name__ == "__main__":

    main()
