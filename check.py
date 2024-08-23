from classes import *
from functions import *
from time import sleep
return_num_ships()
field = create_field()
us_field = create_field()

ship = Ship()

ship.ship_gen(field, 0, True, 89)
print_field(field)
print("--------------------------")
for i in range(len(field)):
    for j in range(len(field)):
        if isinstance(field[i][j], Ship):
            us_field[i][j] = "o"
print_field(us_field)
print("--------------------------")

while True:
    coords = list(map(int, input().split()))
    ship.fire(field, coords)
    print_field(field)
    print("-------------------------")
    for i in range(len(field)):
        for j in range(len(field)):
            if isinstance(field, Ship):
                us_field[i][j] = "o"
    print_field(us_field)
    print("--------------------------")

# ship.fire(field, (7, 0))
# ship.fire(field, (8, 0))
# ship.fire(field, (6, 0))

print_field(field)
return_num_ships()

