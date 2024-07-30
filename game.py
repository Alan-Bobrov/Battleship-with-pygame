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

# цикл под этим коментом отвечает за стартовые корабли бота, можешь его убрать, он так работает временно
for _ in range(10):
    bot_field.bot_play()

# пока что это не нужно, но я это не удалил, мб в будующем пригодится
#for i in range(10):
#    first_num = 476 + 32 * i
#    second_num = first_num + 28
#    y_coords.append((first_num, second_num))
#    x_coords.append((first_num - 366, second_num - 366))

screen = pg.display.set_mode((1024, 900))
screen.fill((255, 255, 255))

OneDeckShipImg = pg.image.load("images/OneDeckShip.png")
ShipStartImg = pg.image.load("images/ShipStart.png")
ShipContinueImg = pg.image.load("images/ShipContinue.png")
ShipEndImg = pg.image.load("images/ShipEnd.png")


# чтобы по этим кораблям стрелять нужно их расставить по другому, а мне это делать лень
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
            #это чтобы стрелять по боту, можешь изменить bot_field на player_field, чтобы стрелять по игроку

    pg.display.flip()

# если хочешь узнать где я работал, заиди в классы и посмотри что я сделал с классами