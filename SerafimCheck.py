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

return_num_ships()

# func for random create_ship()
def random_ship_gen(comp_field, num_of_ships):
    num_of_errors = 0
    while num_of_ships < 10:

        # if num_of_errors >= 200:
        #     num_of_errors = 0
        #     comp_field = create_field()
        #     num_of_ships = 0
        #     return_num_ships()

        result = create_ship(comp_field, (randint(0, 9), randint(0, 9)))
        if not result[0]:
            num_of_errors += 1

        elif result[1] == "new":
            num_of_ships += 1

    return num_of_ships



num_of_ships = 10
random_ship_gen(comp_field, 0)
print_field(comp_field)

while num_of_ships >= 1:
    coords = list(map(int, input().split()))
    result = Ship.fire(Ship, comp_field, coords)
    if result[1] == "Death":
        num_of_ships -= 1
    print_field(comp_field)

# print(comp_field[5][2].start_coords)


