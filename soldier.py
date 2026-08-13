import pygame
from consts import *

class Soldier:
    #ההגדרה של המיקום ההתחלתי
    def __init__(self):
        self.row = 0
        self.col = 0

    def move(self, locationRow, locationCol):
        newRow = self.row + locationRow
        newCol = self.col + locationCol
        if 0 <= newRow and newRow <= (ROWS - SOLDIERHEIGHT):
            self.row = newRow
        if 0 <= newCol and newCol <= (COLS - SOLDIERWIDTH):
            self.col = newCol

    def get_body_cells(self):
        soldierBodyLocations = []
        for i in range(self.row, self.row + 3):
            for j in range(self.col, self.col + SOLDIERWIDTH):
                soldierBodyLocations.append((i, j))
        return soldierBodyLocations

    def get_feet_cells(self):
        feet_cells = []
        legsRow = self.row + 3
        for j in range(self.col, self.col + SOLDIERWIDTH):
            feet_cells.append((legsRow, j))
        return feet_cells