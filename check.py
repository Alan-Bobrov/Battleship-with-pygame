from classes import *
from functions import *
from time import sleep
return_num_ships()
field = create_field()

ship = Ship()

ship.put_ship(field, (6, 0))
ship.put_ship(field, (7, 0))
ship.put_ship(field, (8, 0))

ship.fire(field, (7, 0))
ship.fire(field, (8, 0))
ship.fire(field, (6, 0))

print_field(field)
return_num_ships()

