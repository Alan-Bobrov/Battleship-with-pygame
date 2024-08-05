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