from settings import *
from grid import *
import pygame

pygame.init()

disp = pygame.display
win = disp.set_mode((GRID_WIDTH*RES+1, GRID_HEIGHT*RES+1))
disp.set_caption("Irakli's Minesweeper")

grid = Grid(win, MINE_COUNT, GRID_WIDTH, GRID_HEIGHT)
grid.generate()
grid.add_mines()
grid.update_numbers()

while True:
    win.fill((51, 51, 51))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    grid.draw()
    disp.update()