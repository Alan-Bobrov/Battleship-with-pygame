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

bot_field.do_ships(None, 0, True)
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
field_for_ships = create_field()

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
                changed, x, y = change_coords(x, y)
                if changed:
                    num_of_ships = player_field.do_ships((y, x), num_of_ships, False, field_for_ships)
                    player_field.normal_ships_image()

                if num_of_ships == 10:
                    do_ship = False

            else:
                # if user click on the button and it time when we r putting ships
                if (81 <= x <= 941) and (55 <= y <= 189) and is_putting:
                    clear_field(screen)
                
                end_bots_attack = bot_field.fire_pg(x, y)
                if end_bots_attack[0]:
                    player_field.bot_play()
                    if end_bots_attack[1]:
                        bot_field.death(end_bots_attack[2][0], end_bots_attack[2][1])

    pg.display.flip()