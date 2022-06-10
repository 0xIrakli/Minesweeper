from copy import deepcopy
from settings import *
import random as rand
import pygame

pygame.init()
font = pygame.font.SysFont('chalkduster.ttf', RES)

class Grid:
    def __init__(self, win, mine_count, width, height):
        self.mine_count = mine_count
        self.w = width
        self.h = height
        self.win = win
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

    def draw(self):
        WIN_WIDTH = self.w*RES
        WIN_HEIGHT = self.h*RES
        for x in range(self.w+1):
            pygame.draw.line(self.win, (180, 180, 180), (x*RES, 0), (x*RES, WIN_WIDTH), 2)
        for y in range(self.h+1):
            pygame.draw.line(self.win, (180, 180, 180), (0, y*RES), (WIN_HEIGHT, y*RES), 2)

        for y in range(self.h):
            for x in range(self.w):
                N = str(self.grid[y][x])
                img = font.render(N, True, (120, 210, 120))
                
                if N == '0':
                    img = font.render('', True, (220, 220, 110))
                elif N == '-1':
                    img = font.render('X', True, (220, 110, 110))

                rect = img.get_rect()
                rect.center = (x*RES+RES/2, y*RES+RES/2)
                self.win.blit(img, rect)