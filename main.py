from copy import deepcopy
import random as rand
import pygame
pygame.init()

MINE_COUNT = 10


class Grid:
    def __init__(self, mine_count, width, height):
        self.mine_count = mine_count
        self.w = width
        self.h = height
        self.grid = []

    def generate(self):
        self.grid = []
        for y in range(self.h):
            self.grid.append([])
            for x in range(self.w):
                self.grid[y].append(0)

    def add_mine(self):
        x, y = rand.randrange(self.w), rand.randrange(self.h)
        if self.grid[y][x] == -1:
            self.add_mine()
        else:
            self.grid[y][x] = -1

    def add_mines(self):
        [self.add_mine() for x in range(self.mine_count)]

    def update_numbers(self):
        grid = deepcopy(self.grid)
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] != -1:
                    neighbour_bombs = 0
                    for Y in range(-1, 2):
                        for X in range(-1, 2):
                            xx = min(self.w-1, max(0, x+X))
                            yy = min(self.h-1, max(0, y+Y))
                            neighbour_bombs += self.grid[yy][xx]
                    grid[y][x] = abs(neighbour_bombs)
        self.grid = grid

    def print(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == -1:
                    print(' X', end='')
                else:
                    print(f' {self.grid[y][x]}', end='')
            print('')

grid = Grid(10, 10, 10)
grid.generate()
grid.add_mines()
grid.update_numbers()
grid.print()