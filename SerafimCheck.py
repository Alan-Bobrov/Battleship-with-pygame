import json
from random import randint
from functions import create_field, print_field, return_num_ships
from classes import *


<<<<<<< HEAD
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


=======
class Ship:
    def __init__(self) -> None:
        self.length = 1

    def put_ship(self, comp_field, user_field, coords, is_bot=False):
        string, column = coords

        # check coords 
        if isinstance(string, int) and isinstance(column, int):
            if (string <= -1 or string >= 10) and (column <= -1 or column >= 10) or comp_field[string][column] != "-":
                return False, None
        else:
            return False, None
        
        # check corners of ship
        for i in (1, -1): 
            for j in (1, -1):
                try:
                    if (0 <= string + i <= 9) and (0 <= column + j <= 9):
                        if isinstance(comp_field[string + i][column + j], Ship):
                            return False, None
                except IndexError:
                    continue

        num_of_ships_around = 0

        # check num of ships around coords
        for i in (1, -1):
            
            # check cells sround ship
            try:
                column_cell = comp_field[string][column + i] # there are change only column
            except:
                if column + i >= 10:
                    column_cell = comp_field[string][column]

            try:
                string_cell = comp_field[string + i][column] # there are change only string
            except:
                if string + i >= 10:
                    string_cell = comp_field[string][column]

            # check column cell and srtring cell
            if isinstance(column_cell, Ship):
                if column + i >= 0:
                    num_of_ships_around += 1


            if isinstance(string_cell, Ship):
                if string + i >= 0:
                    num_of_ships_around += 1

        # create new ship
        if num_of_ships_around == 0:
            comp_field[string][column] = self
            with open("num_of_ships.json", "r", encoding="utf-8") as file:
                num_of_ships = json.load(file)
                if num_of_ships["1"] <= 0:
                    comp_field[string][column] = "-"
                    #print(9)
                    return False, None
                num_of_ships["1"] -= 1
                with open("num_of_ships.json", "w", encoding="utf-8") as file1:
                    json.dump(num_of_ships, file1, indent=4)
            if not is_bot:
                user_field[string][column] = "*"
            return True, "new"

        # continue ship
        elif num_of_ships_around == 1:

            # check continue of ship
            for i in (1, -1):
                try:
                    column_cell = comp_field[string][column + i] # there are change only column
                except IndexError:
                    if (column + i >= 10) or (column + i <= -1):
                        column_cell = comp_field[string][column]

                try:
                    string_cell = comp_field[string + i][column] # there are change only string
                except IndexError:
                    if (string + i >= 10) or (string + i <= -1):
                        string_cell = comp_field[string][column]

                
                # if horizontal ship
                if isinstance(column_cell, Ship):
                    comp_field[string][column] = column_cell

                    if (column_cell.length + 1 == comp_field[string].count(column_cell)) and (column_cell.length + 1 <= 4):
                        column_cell.length += 1
                        if not is_bot:
                            user_field[string][column] = "*"
                        if not update_num_of_ships(column_cell):
                            column_cell.length -= 1
                            comp_field[string][column] = "-"
                            user_field[string][column] = "-"
                            return False, None
                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    return True, ("Right" if i == 1 else "Left")

                # if vertical ship
                if isinstance(string_cell, Ship):
                    column_values = list()
                    for i in range(10):
                        column_values.append(comp_field[i][column])
                    
                    comp_field[string][column] = string_cell
                    if (string_cell.length == column_values.count(string_cell)) and (string_cell.length + 1 <= 4):
                        string_cell.length += 1
                        if not is_bot:
                            user_field[string][column] = "*"
                        if not update_num_of_ships(string_cell):
                            string_cell.length -= 1
                            comp_field[string][column] = "-"
                            user_field[string][column] = "-"
                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    return True, ("Down" if i == 1 else "Up")

        return False, None

    # func for put ship on comp field
    def create_ship(comp_field, user_field, coords):
        ship = Ship()
        result = ship.put_ship(comp_field, user_field, coords)
        return result
    
    # func for random create_ship()
    def random_ship_gen(comp_field, user_field, num_of_ships):
        while num_of_ships < 10:
            result = Ship.create_ship(comp_field, user_field, (randint(0, 9), randint(0, 9)))
            if result[1] == "new":
                num_of_ships += 1
                
        return num_of_ships
return_num_ships()



# print("---------------------------------------")
# print_field(comp_field)
>>>>>>> bfdddeb30d86aca895f955c62daa26e63f85e733

comp_field = create_field()
user_field = create_field()


Ship.random_ship_gen(comp_field, user_field, 0)
print_field(user_field)

