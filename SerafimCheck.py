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

random_ship_gen(comp_field, num_of_ships)

Ship.fire(Ship, comp_field, (0, 7))

print_field(comp_field)



comp_field = create_field()
user_field = create_field()


