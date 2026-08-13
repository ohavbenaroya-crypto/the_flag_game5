import pygame
from consts import *
from screen import Screen
from soldier import Soldier
from game_field import GameField
import time


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
    is_running = True

    while is_running:
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
        #
        if show_mines:
            screen.draw_grid()
            screen.draw_landmines(field.landmines)
            screen.draw_soldier_nigth(soldier.row, soldier.col)
# הגדרתי את החייל לילה בכונסטאס ובסקרין והוספתי פעולה של ציור חייל לילה ופשוט מחקתי את הציור חייל שהיה לא בתוך לולאה אל האלס ואת ציור חייל לילה ב if
        else:
            screen.draw_flag(field.flag_row, field.flag_col)
            screen.draw_bushes(field.bushes)
            screen.draw_soldier(soldier.row, soldier.col)
# מחקתי את הציור דגל מחוץ ללולאה אל הלולאה של ה else

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