import pygame
from consts import *
import time


class Screen:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.display = pygame.display.set_mode((GAMEWIDTH, GAMEHEIGHT))
        pygame.display.set_caption("The Flag")
        self.soldier_img = self.load_image(SOLDIERIMAGE, SOLDIERWIDTH, SOLDIERHEIGHT)
        self.soldier_nigth_img = self.load_image(SOLDIERNIGTHIMAGE, SOLDIERWIDTH,SOLDIERHEIGHT)
        self.flag_img = self.load_image(FLAGIMAGE, FLAGWIDTH, FLAGHEIGHT)
        self.landmine_img = self.load_image(LANDMINESIMAGE, LANDMINEWIDTH, LANDMINEHEIGHT)
        self.bush_img = self.load_image(BUSHIMAGE, 2, 2)
        self.font = pygame.font.SysFont("Arial", 28)

    def load_image(self, path, width_cells, height_cells):
        img = pygame.image.load(path)
        new_width = width_cells * SQUARESIZE
        new_height = height_cells * SQUARESIZE
        return pygame.transform.scale(img, (new_width, new_height))

    def clear(self):
        self.display.fill(GREEN)
##
    def draw_grid(self):


        self.display.fill(BLACK)
        for i in range(ROWS + 1):
            pygame.draw.line(self.display, GREEN, (0, i * SQUARESIZE), (GAMEWIDTH, i * SQUARESIZE))
        for j in range(COLS + 1):
            pygame.draw.line(self.display, GREEN, (j * SQUARESIZE, 0), (j * SQUARESIZE, GAMEHEIGHT))
##
    def draw_bushes(self, bushes):
        for i, j in bushes:
            self.display.blit(self.bush_img, (j * SQUARESIZE, i * SQUARESIZE))

    def draw_flag(self, flag_row, flag_col):
        self.display.blit(self.flag_img, (flag_col * SQUARESIZE, flag_row * SQUARESIZE))

    def draw_soldier(self, soldier_row, soldier_col):
        self.display.blit(self.soldier_img, (soldier_col * SQUARESIZE, soldier_row * SQUARESIZE))

    def draw_soldier_nigth(self, soldier_row, soldier_col):
        self.display.blit(self.soldier_nigth_img, (soldier_col * SQUARESIZE, soldier_row * SQUARESIZE))

    def draw_landmines(self, landmines):
        for i, j in landmines:
            self.display.blit(self.landmine_img, (j * SQUARESIZE, i * SQUARESIZE))

    def draw_welcome_message(self):
        text = self.font.render("Welcome to The Flag game. Have Fun!", True, WHITE)
        self.display.blit(text, (100, 10))

    def draw_message(self, message, color):
        text = self.font.render(message, True, color)
        rect = text.get_rect(center=(GAMEWIDTH // 2, GAMEHEIGHT // 2))
        self.display.blit(text, rect)

    def update(self):
        pygame.display.flip()