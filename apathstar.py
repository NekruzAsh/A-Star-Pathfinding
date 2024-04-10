
# author: Nekruz Ashrapov
# date: 4/8/2024 

import pygame
import math
from queue import PriorityQueue



WIDTH = 900
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A star path algorithm")

RED = (255, 0, 0)           #constant values don't change
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = GREY             #<---- spots starting color
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        

    
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == BLUE       # <----- spot already looked at

    def is_open(self):
        return self.color == GREEN  # <--- open set

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == TURQUOISE

    def is_end(self):
        return self.color == WHITE

    def reset(self):
        self.color = GREY

    def make_start(self):
        self.color = TURQUOISE
        
    def make_closed(self):
        self.color = BLUE

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = WHITE

    def make_path(self):
        self.color = RED        #<--- Finished PATH

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():     # checking going down 0 - 4 etc
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():     # checking going up
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():     # checking going Right
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():     # checking going Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


    
