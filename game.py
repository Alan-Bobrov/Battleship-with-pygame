import pygame as pg
from classes import *

pg.init()

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

OneDeckShipImg = pg.image.load("images/OneDeckShip.png")
ShipStartImg = pg.image.load("images/ShipStart.png")
ShipContinueImg = pg.image.load("images/ShipContinue.png")
ShipEndImg = pg.image.load("images/ShipEnd.png")



screen.blit(FieldImg, (0, 0))
screen.blit(SkipImg, (142, 476))
screen.blit(HitImg, (110, 476))

screen.blit(OneDeckShipImg, (110, 508))

screen.blit(ShipStartImg, (110, 604))
screen.blit(ShipContinueImg, (110, 570))
screen.blit(ShipEndImg, (110, 540))

screen.blit(HitImg, (110, 508))

is_game = True
while is_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
    
    pg.display.flip()

