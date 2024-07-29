import pygame as pg
from classes import *

pg.init()

x_coords = []
y_coords = []

for i in range(10):
    first_num = 476 + 32 * i
    second_num = first_num + 28
    y_coords.append((first_num, second_num))
    x_coords.append((first_num - 366, second_num))

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

OneDeckShipImg = pg.image.load("images/OneDeckShip.png")
ShipStartImg = pg.image.load("images/ShipStart.png")
ShipContinueImg = pg.image.load("images/ShipContinue.png")
ShipEndImg = pg.image.load("images/ShipEnd.png")



screen.blit(FieldImg, (0, 0))
# screen.blit(SkipImg, (142, 476))
# screen.blit(HitImg, (110, 476))

# screen.blit(OneDeckShipImg, (110, 508))

# screen.blit(ShipStartImg, (110, 604))
# screen.blit(ShipContinueImg, (110, 570))
# screen.blit(ShipEndImg, (110, 540))


# screen.blit(HitImg, (110, 508))

for i in y_coords:
    for j in x_coords:
        screen.blit(OneDeckShipImg, (j[0], 476))

is_game = True
while is_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            for iy in range(10):
                for jx in range(10):
                    if (x_coords[jx][0] <= x <= x_coords[jx][1]) and (y_coords[iy][0] <= y <= y_coords[iy][1]):
                        screen.blit(OneDeckShipImg, (x_coords[jx][0], y_coords[iy][0]))
    
    pg.display.flip()

