import pygame as pg
from classes import *
from functions import *
from images import *

pg.init()

player_field = Field(110, 476)
bot_field = Field(598, 476)


bot_field.bot_do_ships()
bot_field.normal_ships_image()

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

screen.blit(FieldImg, (0, 0))

is_game = True
while is_game:
    player_field.pr_all(screen, print_ships=True)
    bot_field.pr_all(screen, print_ships=True)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            end_bots_attack = bot_field.fire_pg(x, y)
            if end_bots_attack[0]:
                player_field.bot_play()
                if end_bots_attack[1]:
                    bot_field.death(end_bots_attack[2][0], end_bots_attack[2][1])

    pg.display.flip()