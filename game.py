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
is_again = False
is_putting = True
is_game = True
while is_game:
    player_field.pr_all(screen, print_ships=True)
    bot_field.pr_all(screen, print_ships=True)
    SetClearButton(screen, is_putting)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos() # 467, 560
            if (81 <= x <= 941) and (55 <= y <= 189) and is_putting:
                clear_field(screen)
            end_bots_attack = bot_field.fire_pg(x, y)
            if end_bots_attack[0]:
                player_field.bot_play()
                if end_bots_attack[1]:
                    bot_field.death(end_bots_attack[2][0], end_bots_attack[2][1])

    pg.display.flip()