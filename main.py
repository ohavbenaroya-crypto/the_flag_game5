from operator import index

import pygame
import time

import consts
from consts import *
from screen import Screen
from soldier import Soldier
from game_field import GameField

# def Buttons(key_pres):   #פונקציה שמחשבת את המיקום של אותו מיקום של מספר
#  input = ''
#  cont = 0
#  # for event in pygame.event.get():
#  #    if event.type == pygame.QUIT:
#  #         running = False
#
#  for i in buttons:
#         if i == key_pres:
#             break
#         else: cont+= 1
#  return cont



def main():
    screen = Screen()
    field = GameField()
    soldier = Soldier()
    clock = pygame.time.Clock()



    show_mines = False
    mines_timer = 0
    is_game_over = False
    message = ""
    message_color = WHITE
    running = True

    the_key = 0
    # זיהוי של הממספר שהשחקן רוצה ללחוץ

    while running:
        current_time = pygame.time.get_ticks()

        if show_mines:
                if current_time - mines_timer >= 1000:
                  show_mines = False

        for event in pygame.event.get(): #בדיקת אירועים ומקשים שהשחקן לוחץ במיקלדת ולפיהם לפעול בהתאם
                      if event.type == pygame.QUIT: #אם  השחקן רוצה לעצור את המישחק תפסיק ללרוץ
                          is_running = False
                      if event.type == pygame.KEYDOWN: #זיהוי לחיצה במקלדת
                          if is_game_over == False:
                              if show_mines == False:
                                  if event.key == pygame.K_UP:
                                      soldier.move(-1, 0)
                                  elif event.key == pygame.K_DOWN:
                                      soldier.move(1, 0)
                                  elif event.key == pygame.K_LEFT:
                                      soldier.move(0, -1)
                                  elif event.key == pygame.K_RIGHT:
                                      soldier.move(0, 1)

                              if event.key == pygame.K_RETURN:
                                  show_mines = True
                                  mines_timer = current_time



                              if event.key == pygame.K_0 - the_key: #מדידת זמן של לחיצה על אחד המספרים
                                t = time.time()
                      if event.type == pygame.KEYUP:
                          if event.key == pygame.K_0 - the_key:  # key 'a'
                              t = time.time() - t;t = str(t); t = t[:5]
                              print("You pressed key 'a' for", t, 'seconds')


        if is_game_over == False:  #התאמה של הרגלים והגוף של השחקן לריבועים במטריצה
            feet_cells = soldier.get_feet_cells()
            body_cells = soldier.get_body_cells()

            if field.check_mine(feet_cells): #בדיקת ניצחון \ הפסד - בדיקה אם הרגלים של השחקן נגעו בפצצה\דגל
                is_game_over = True
                message = "You Lost!"
                message_color = RED
            elif field.check_flag(body_cells):
                is_game_over = True
                message = "You Won!"
                message_color = WHITE

        screen.clear()
#ציור של אלמנטים על פני המסך
        if show_mines:
            screen.draw_grid()
            screen.draw_landmines(field.landmines)
            screen.draw_soldier_nigth(soldier.row, soldier.col)
        else:
            screen.draw_bushes(field.bushes)
            screen.draw_flag(field.flag_row, field.flag_col)
            screen.draw_soldier(soldier.row, soldier.col)
            screen.draw_welcome_message()


#בדיקת זמן אחרי שהמשחק נגמר בשביל לדעת אחרי כמה שניות לסגור את החלון
        if is_game_over:
            screen.draw_message(message, message_color)
            screen.update()
            pygame.time.wait(3000)
            is_running = False
        else:
            screen.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
