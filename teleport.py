import random
from consts import *

from pip._internal import locations

import consts
import game_field

HOLESIMAGE = "mine.png"
Number_of_holes = 5
Locations_of_holes = []
places_launching = []
flag_col = COLS - FLAGWIDTH
flag_row = ROWS - FLAGHEIGHT
for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)




    for run in range(Number_of_holes):

            i = random.randint(0, consts.ROWS -3)
            j = random.randint(0, consts.COLS -1 )
            Locations_of_holes.append([i,j])


# def check_hole(feet_list): #פונקציה לבדיקה אם השחקן דרך דרך על הטלפורט
#             for row, col in feet_list:
#                 if row >= 0 and row < consts.ROWS and col >= 0 and col < consts.COLS:
#                     if grid[row][col] == 1:
#                         return True
#             return False

# def generate_place_launching():
#     i = random.randint(0, consts.ROWS - 1)
#     j = random.randint(0, consts.COLS - 1)
#     places_launching.append((i,j))















