import json
from random import randint

def return_num_ships():
    object = {
        "4": 1,
        "3": 2,
        "2": 3,
        "1": 4
    }
    with open("num_of_ships.json", "w", encoding="utf-8") as file:
        json.dump(object, file, indent=4)

def create_field(space_symbol="-"):
    field = [[space_symbol for _ in range(10)] for i in range(10)]
    return field

def print_field(field):
    for i in range(len(field)):
        print(*field[i])

def update_num_of_ships(cell):
    with open("num_of_ships.json", "r", encoding="utf-8") as num_of_ships:
        num_of_ships = json.load(num_of_ships)
        try:
            if num_of_ships[f"{cell.length}"] < 1:
                return False
            num_of_ships[f"{cell.length - 1}"] += 1
            num_of_ships[f"{cell.length}"] -= 1
        except:
            pass
        else:
            with open("num_of_ships.json", "w", encoding="utf-8") as file:
                json.dump(num_of_ships, file, indent=4)
    return True

comp_field = create_field()
user_field = create_field()

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
                    if isinstance(comp_field[string + i][column + j], Ship):
                        return False, None
                except IndexError:
                    continue

        num_of_ships_around = 0

        # check num of ships around coords
        for i in (1, -1):
            try:
                column_cell = comp_field[string][column + i] # there are change only column
                string_cell = comp_field[string + i][column] # there are change only string
            except:
                continue

            if isinstance(column_cell, Ship):
                if column + i > -1:
                    num_of_ships_around += 1

            if isinstance(string_cell, Ship):
                if string + i > -1:
                    num_of_ships_around += 1
        
        # create new ship
        if num_of_ships_around == 0:
            comp_field[string][column] = self
            with open("num_of_ships.json", "r", encoding="utf-8") as file:
                num_of_ships = json.load(file)
                if num_of_ships["1"] <= 0:
                    comp_field[string][column] = "-"
                    # print(9)
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
                    if (string + i <= -1) or (column + i <= -1):
                        raise IndexError
                    column_cell = comp_field[string][column + i] # there are change only column
                    string_cell = comp_field[string + i][column] # there are change only string
                except:
                    continue
                
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
                        # print(1)
                        comp_field[string][column] = "-"
                        return False, None

        return False, None

return_num_ships()

def create_ship(comp_field, user_field, coords):
    ship = Ship()
    result = ship.put_ship(comp_field, user_field, coords)
    return result

num_of_ships = 0
count = 0

def random_ship_gen(comp_field, user_field, num_of_ships):
    while num_of_ships < 10:
        result = create_ship(comp_field, user_field, (randint(0, 9), randint(0, 9)))
        if result[1] == "new":
            num_of_ships += 1
    return num_of_ships

random_ship_gen(comp_field, user_field, num_of_ships)

# create_ship(comp_field, user_field, (0, 4))
# create_ship(comp_field, user_field, (1, 4))
# create_ship(comp_field, user_field, (2, 4))
# create_ship(comp_field, user_field, (3, 4))

# create_ship(comp_field, user_field, (0, 0))
# create_ship(comp_field, user_field, (0, 1))
# create_ship(comp_field, user_field, (2, 0))
# create_ship(comp_field, user_field, (2, 1))
# create_ship(comp_field, user_field, (4, 0))
# create_ship(comp_field, user_field, (4, 1))
# create_ship(comp_field, user_field, (6, 0))

# create_ship(comp_field, user_field, (6, 1))
# create_ship(comp_field, user_field, (8, 5))
# create_ship(comp_field, user_field, (0, 9))
# create_ship(comp_field, user_field, (9, 9))
# create_ship(comp_field, user_field, (7, 7))

# create_ship(comp_field, user_field, (0, 2))

# create_ship(comp_field, user_field, (8, 9))
# create_ship(comp_field, user_field, (7, 9))



print_field(user_field)
print("---------------------------------------")
print_field(comp_field)

