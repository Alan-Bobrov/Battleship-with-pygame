import pygame as pg

pg.init()

screen = pg.display.set_mode((1400, 800))
screen.fill((255, 255, 255))

is_game = True
while is_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
    
    pg.display.flip()

