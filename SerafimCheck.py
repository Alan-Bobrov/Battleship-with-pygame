import json
from random import randint
from functions import create_field, print_field, return_num_ships
from classes import *

comp_field = create_field()

# func for put ship on comp field
def create_ship(comp_field, coords):
    ship = Ship()
    result = ship.put_ship(comp_field, coords)
    return result
    
# func for random create_ship()
def random_ship_gen(comp_field, num_of_ships):
    while num_of_ships < 10:
        result = create_ship(comp_field, (randint(0, 9), randint(0, 9)))
        if result[1] == "new":
            num_of_ships += 1
    return num_of_ships

return_num_ships()

num_of_ships = 0

# random_ship_gen(comp_field, num_of_ships)

col = 5
var = 4
ship_len = 4


for i in range(ship_len):
    create_ship(comp_field, (col, i + 2))

for i in range(ship_len):
    Ship.fire(Ship, comp_field, (col, i + 2))

create_ship(comp_field, (9, 9))

Ship.fire(Ship, comp_field, (9, 9))

print_field(comp_field)
# print(comp_field[5][2].start_coords)


