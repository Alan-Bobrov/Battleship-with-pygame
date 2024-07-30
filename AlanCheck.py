import pygame as pg
from classes import *
from functions import *

player_field = Field(110, 476)
bot_field = Field(598, 476)
for _ in range(10):
    bot_field.bot_play()

pg.init()


#x_coords = []
#y_coords = []
# our field: - 366
# enemy field: + 122


#for i in range(10):
#    first_num = 476 + 32 * i
#    second_num = first_num + 28
#    y_coords.append((first_num, second_num))
#    x_coords.append((first_num + 122, second_num + 122))

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))



OneDeckShipImg = pg.image.load("images/OneDeckShip.png")
ShipStartImg = pg.image.load("images/ShipStart.png")
ShipContinueImg = pg.image.load("images/ShipContinue.png")
ShipEndImg = pg.image.load("images/ShipEnd.png")

screen.blit(FieldImg, (0, 0))
# screen.blit(SkipImg, (142, 476))
# screen.blit(HitImg, (110, 476))
screen.blit(OneDeckShipImg, (110, 508))
screen.blit(ShipStartImg, (110, 604))
screen.blit(ShipContinueImg, (110, 570))
screen.blit(ShipEndImg, (110, 540))




is_game = True
while is_game:
    player_field.pr_all(screen)
    bot_field.pr_all(screen, print_ships=True)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos() # 467, 560
            bot_field.fire_pg(x, y)
            

                            
    pg.display.flip()