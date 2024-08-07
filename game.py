# automaticly pip install pygame
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
except:
    pass

import pygame as pg
from classes import *
from functions import *
from images import *
import subprocess
import sys


pg.init()

player_field = Field(110, 476)
bot_field = Field(598, 476)

<<<<<<< Updated upstream
bot_field.do_ships(None, 0, True)
=======

bot_comp_field = create_field()
bot_field.do_ships(None, 0, True, bot_comp_field)
>>>>>>> Stashed changes
bot_field.normal_ships_image()
return_num_ships()
screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

screen.blit(FieldImg, (0, 0))

is_again = False # is it end of the game
is_putting = True
is_game = True
num_of_ships = 0
do_ship = True
player_comp_field = create_field()

while is_game:
    screen.blit(FieldImg, (0, 0))
    player_field.pr_all(screen, print_ships=True)
    bot_field.pr_all(screen, print_ships=True)

    # put clear button on the screen
    SetClearButton(screen, is_putting)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos() # 467, 560

            if do_ship:
                changed, x, y = change_coords(x, y, 110, 476)
                if changed:
                    num_of_ships = player_field.do_ships((y, x), num_of_ships, False, player_comp_field)
                    player_field.normal_ships_image()

                if num_of_ships == 10:
                    do_ship = False

            else:
                changed, x, y = change_coords(x, y, 598, 476)
                # if user click on the button and it time when we r putting ships
                if (81 <= x <= 941) and (55 <= y <= 189) and is_putting:
                    clear_field(screen)
                
                if changed and bot_field.field[y][x].status in ("free_place", "part_ship"):
                    s = Ship()
                    players_attack_result = s.fire(bot_comp_field, (y, x))
                    bot_field.synchronize(x, y)
                    bot_field.synchronize(x, y, bot_comp_field)
                    if players_attack_result[0] == False:
                        bot_move = (True,)
                        while bot_move[0]:
                            while True:
                                coords = (randint(0, 9), randint(0, 9)) # y x
                                if type(player_comp_field[coords[0]][coords[1]]) == Ship or player_comp_field[coords[0]][coords[1]] == "-":
                                    break
                            print_field(bot_comp_field)
                            bot_move = s.fire(player_comp_field, (coords[0], coords[1]))
                            player_field.synchronize(coords[1], coords[0])
                            player_field.synchronize(coords[1], coords[0], player_comp_field)

    pg.display.flip()