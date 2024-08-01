import pygame as pg
from classes import *
from functions import *

pg.init()

#x_coords = []
#y_coords = []
# our field: - 366
# enemy field: + 122

player_field = Field(110, 476)
bot_field = Field(598, 476)

# цикл под этим коментом отвечает за стартовые корабли и бота и игрока, можешь его убрать, он так работает временно
for _ in range(10):
    bot_field.bot_do_ships()
for _ in range(10):
    player_field.bot_do_ships()

# пока что это не нужно, но я это не удалил, мб в будующем пригодится
#for i in range(10):
#    first_num = 476 + 32 * i
#    second_num = first_num + 28
#    y_coords.append((first_num, second_num))
#    x_coords.append((first_num - 366, second_num - 366))

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

#OneDeckShipImg = pg.image.load("images/OneDeckShip.png")
#ShipStartImg = pg.image.load("images/ShipStart.png")
#ShipContinueImg = pg.image.load("images/ShipContinue.png")
#ShipEndImg = pg.image.load("images/ShipEnd.png")

screen.blit(pg.image.load("images/Field.png"), (0, 0))

is_game = True
while is_game:
    player_field.pr_all(screen, print_ships=True)
    bot_field.pr_all(screen, print_ships=True)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos() # 467, 560
            end_attack = bot_field.fire_pg(x, y)
            if end_attack[0]:
                player_field.bot_play()
                if end_attack[1]:
                    bot_field.death(x, y)

    pg.display.flip()