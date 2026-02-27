import pygame
import math
from queue import PriorityQueue

# initialize pygame
pygame.init()

# title of the window
pygame.display.set_caption('Dynamic Path Finding Agent')

# ask user for grid size
# keeping it like a square so don't have to deal
# with height variables
size = int(input("Please give size for grid: "))

screen = pygame.display.set_mode((size, size))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self. col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE      # all white nodes at start
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    # red nodes/squares (already explored)
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == PURPLE
    
    def reset(self):
        return self.color == WHITE
    
    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    # lt means less than and it is being used to compare two nodes
    def __lt__(self, other):
        return False

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()