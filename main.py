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



# def conting_butuns_time(event):
#     start_time = None
#     press_duration = 0
#
#     if event == pygame.KEYDOWN and event.key == pygame.K_1:
#         start_time = pygame.time.get_ticks()
#
#     if event == pygame.KEYUP and event.key == pygame.K_1:
#             press_duration = pygame.time.get_ticks() - start_time
#
#     return press_duration
#




# def cont_time_buttons():
#     pygame.init()
#     clock = pygame.time.Clock()
#
#     start_time = None
#     press_duration = 0
#
#     # running = True
#     # while running:
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
#               start_time = pygame.time.get_ticks()
#
#             if event.type == pygame.KEYUP and event.key == pygame.K_1:
#                 press_duration = pygame.time.get_ticks() - start_time
#                 time_cont=press_duration/1000
#
#         # clock.tick(60)




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

        for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                          is_running = False
                      if event.type == pygame.KEYDOWN:
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



                              if event.key == pygame.K_0 - the_key:
                                t = time.time()
                      if event.type == pygame.KEYUP:
                          if event.key == pygame.K_0 - the_key:  # key 'a'
                              t = time.time() - t;t = str(t); t = t[:5]
                              print("You pressed key 'a' for", t, 'seconds')


        if is_game_over == False:
            feet_cells = soldier.get_feet_cells()
            body_cells = soldier.get_body_cells()

            if field.check_mine(feet_cells):
                is_game_over = True
                message = "You Lost!"
                message_color = RED
            elif field.check_flag(body_cells):
                is_game_over = True
                message = "You Won!"
                message_color = WHITE

        screen.clear()

        if show_mines:
            screen.draw_grid()
            screen.draw_landmines(field.landmines)
            screen.draw_soldier_nigth(soldier.row, soldier.col)
        else:
            screen.draw_bushes(field.bushes)
            screen.draw_flag(field.flag_row, field.flag_col)
            screen.draw_soldier(soldier.row, soldier.col)
            screen.draw_welcome_message()



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
