from .constants import WHITE, GREEN, YELLOW, BLACK, WIDTH, HEIGHT
from dataclasses import dataclass
import pygame as pg


@dataclass
class Tile:

    row: int
    col: int
    width: int
    root: pg.Surface
    color: tuple[int, int, int] = WHITE

    def __post_init__(self) -> None:
        self.x = self.row * self.width
        self.y = self.col * self.width
        self.rect = (self.x, self.y, self.width, self.width)

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
