import random
from consts import *
class GameField:
    def __init__(self):
        self.grid = []
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                row.append(0)
            self.grid.append(row)
        self.landmines = []
        self.bushes = []
        self.flag_row = ROWS - FLAGHEIGHT
        self.flag_col = COLS - FLAGWIDTH
        self.generate_bushes()
        self.generate_landmines()

    def generate_bushes(self):
        count = 0
        while count < NUMBUSHES:
            # row = random.randint(0, ROWS - BUSHESHEIGHT)
            # col = random.randint(0, COLS - BUSHESWIDTH)
            row = 21
            col = 46
            if not (row < 4 and col < 4) and not (row >= self.flag_row and col >= self.flag_col):
                has_bushes = False
                for i in range(col, col + BUSHESWIDTH):
                    if self.grid[row][i] == 1:
                        has_bushes = True
                if has_bushes == False:
                    for i in range(col, col + BUSHESWIDTH):
                        self.grid[row][i] = 1
                    self.bushes.append((row, col))
                    count = count + 1


        # for run in range(NUMBUSHES):
        #     i = random.randint(0, ROWS - 2)
        #     j = random.randint(0, COLS - 2)
        #     while self.grid[i][j] != self.grid[22][46] and self.grid[i][j] != self.grid[21][49]:
        #         i = random.randint(0, ROWS - 2)
        #         j = random.randint(0, COLS - 2)
        #     self.bushes.append((i, j))

    def generate_landmines(self):
        count = 0
        while count < NUMLANDMINES:
            row = random.randint(0, ROWS - LANDMINEHEIGHT)
            col = random.randint(0, COLS - LANDMINEWIDTH)
            if not (row < 4 and col < 4) and not (row >= self.flag_row and col >= self.flag_col):
                has_mine = False
                for i in range(col, col + LANDMINEWIDTH):
                    if self.grid[row][i] == 1:
                        has_mine = True
                if has_mine == False:
                    for i in range(col, col + LANDMINEWIDTH):
                        self.grid[row][i] = 1
                    self.landmines.append((row, col))
                    count = count + 1

    def get_flag_cells(self):
        cells = []
        for i in range(self.flag_row, self.flag_row + FLAGHEIGHT):
            for j in range(self.flag_col, self.flag_col + FLAGWIDTH):
                cells.append((i, j))
        return cells

    def check_mine(self, feet_list):
        for row, col in feet_list:
            if row >= 0 and row < ROWS and col >= 0 and col < COLS:
                if self.grid[row][col] == 1:
                    return True
        return False

    def check_flag(self, body_list):
        flag_list = self.get_flag_cells()
        for cell in body_list:
            if cell in flag_list:
                return True
        return False
