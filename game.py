# automaticly pip install pygame
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
except:
    pass

import pygame as pg
from classes import *
from functions import *
from images import *
from time import sleep
import subprocess
import sys

def game():
    pg.init()

    player_field = Field(110, 476)
    bot_field = Field(598, 476)

    # bot arranges ships
    bot_comp_field = create_field()
    bot_field.do_ships(None, 0, True, bot_comp_field)
    bot_field.normal_ships_image()
    return_num_ships()

    screen = pg.display.set_mode((1024, 900))
    screen.fill((255, 255, 255))

    is_again = False # is it end of the game
    is_game = True
    num_of_ships = 0 # number of ships the player has placed
    do_ship = True # is the player currently placing ships
    player_comp_field = create_field()
    player_ship_count = 0
    bot_ship_count = 0
    first_move = False
    can_go = True
    while is_game:
        
        # field print
        screen.blit(FieldImg, (0, 0))
        player_field.pr_all(screen, print_ships=True)
        bot_field.pr_all(screen, print_ships=True)

        # put clear button on the screen
        screen.blit(RestartImg, (0, 0))

        for i in player_field.field:
            for j in i:
                if j.status == "part_ship":
                    player_ship_count += 1
        for i in bot_field.field:
            for j in i:
                if j.status == "part_ship":
                    bot_ship_count += 1

        if  player_ship_count == 0 and first_move:
            # the message "You lose!" appears here
            screen.blit(YouLoseImg, (0, 0))
            can_go = False
        if  bot_ship_count == 0  and first_move:
            # the message "You win!" appears here
            screen.blit(YouWinImg, (0, 0))
            can_go = False

        player_ship_count = 0    
        bot_ship_count = 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif (event.type == pg.MOUSEBUTTONDOWN) and (pg.mouse.get_pressed(num_buttons=3)[0]):
                x, y = pg.mouse.get_pos()

                # restart the game
                if (81 <= x <= 941) and (55 <= y <= 189):
                        player_field = Field(110, 476)
                        bot_field = Field(598, 476)
                        bot_comp_field = create_field()
                        bot_field.do_ships(None, 0, True, bot_comp_field)
                        bot_field.normal_ships_image()
                        return_num_ships()
                        num_of_ships = 0
                        do_ship = True
                        player_comp_field = create_field()
<<<<<<< HEAD
                        first_move = False
                        can_go = True
=======
                        screen = pg.display.set_mode((1024, 900))
                        screen.fill((255, 255, 255))
>>>>>>> 447d008331c803370b22e8b8312de3440d3ee0e0

                # player arranges ships
                if do_ship:
                    changed, x, y = change_coords(x, y, 110, 476)
                    if changed:
                        num_of_ships = player_field.do_ships((y, x), num_of_ships, False, player_comp_field)
                        player_field.normal_ships_image()

                    if num_of_ships == 10:
                        # the player completes the placement of ships
                        return_num_ships()
                        do_ship = False

                elif can_go:
                    changed, x, y = change_coords(x, y, 598, 476)
                    if changed and bot_field.field[y][x].status in ("free_place", "part_ship"):
                        s = Ship()

                        # the player makes a move
                        players_attack_result = s.fire(bot_comp_field, (y, x))
                        bot_field.synchronize(x, y)
                        bot_field.synchronize(x, y, bot_comp_field)
                        first_move = True
                        # if the player misses, then the bot's turn begins
                        if players_attack_result[0] == False:
                            bot_move = (True,)
                            while bot_move[0]:
                                # the bot chooses the place where it goes
                                while True: 
                                    coords = (randint(0, 9), randint(0, 9)) # y x
                                    if type(player_comp_field[coords[0]][coords[1]]) == Ship or player_comp_field[coords[0]][coords[1]] == "-":
                                        break

                                # the bot makes a move on the place that he has chosen in advance
                                bot_move = s.fire(player_comp_field, (coords[0], coords[1]))
                                player_field.synchronize(coords[1], coords[0])
                                player_field.synchronize(coords[1], coords[0], player_comp_field)
                                sleep(0.125)

        pg.display.flip()

game()