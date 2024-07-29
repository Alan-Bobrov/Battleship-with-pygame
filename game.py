import pygame as pg
from classes import *

pg.init()

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

screen.blit(FieldImg, (0, 0))
screen.blit(SkipImg, (142, 476))

is_game = True
while is_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
    
    pg.display.flip()

