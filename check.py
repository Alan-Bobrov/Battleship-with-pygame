from classes import *
from functions import *
from time import sleep

field = create_field()

while True:
    Ship.ship_gen(field, 0, True, 0)
    for i in range(len(field)):
        for j in range(len(field)):
            if isinstance(field[i][j], Ship):
                field[i][j] = "o"
    print_field(field)
    print("--------------------")
    field= create_field()
    input()
    return_num_ships()



