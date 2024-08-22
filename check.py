from classes import *
from functions import *
from time import sleep

return_num_ships()

field = create_field()

while True:
    num_of_ships = 0
    num_of_errors = 0
    while num_of_ships < 10:

        if num_of_errors >= 300:
            num_of_errors = 0
            num_of_ships = 0
            field = create_field()
            return_num_ships()
        
        ship = Ship()
        result = ship.put_ship(field, (randint(0, 9), randint(0, 9)))

        if not result[0]:
            num_of_errors += 1
        
        if result[1] == "new":
            num_of_ships += 1

    print_field(field)
    print("------------------------------")
    for i in range(len(field)):
        for j in range(len(field)):
            if isinstance(field[i][j], Ship):
                field[i][j] = "o"
    print_field(field)
    print("--------------------")
    
    input()
    field = create_field()
    return_num_ships()

# return_num_ships()

# ship = Ship()
# ship.put_ship(field, (0, 8))

# ship = Ship()
# ship.put_ship(field, (2, 5))

# ship = Ship()
# ship.put_ship(field, (7, 0))

# ship = Ship()
# ship.put_ship(field, (0, 1))

# ship = Ship()
# ship.put_ship(field, (0, 0))

# print_field(field)

# return_num_ships()