def create_field(space_symbol="-"):
    field = [[space_symbol for _ in range(10)] for i in range(10)]
    return field

def print_field(field):
    for i in range(len(field)):
        print(*field[i])

comp_field = create_field()
user_field = create_field()

class Ship:
    def __init__(self) -> None:
        self.length = 1

    def put_ship(self, comp_field, user_field, coords, is_bot=False):
        string, column = coords

        # check coords 
        if isinstance(string, int) and isinstance(column, int):
            if (string <= -1 or string >= 10) and (column <= -1 or column >= 10):
                return False
        else:
            return False
        
        # check corners of ship
        for i in (1, -1):
            for j in (1, -1):
                try:
                    if isinstance(comp_field[string + i][column + j], Ship):
                        return False
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
                num_of_ships_around += 1

            if isinstance(string_cell, Ship):
                num_of_ships_around += 1
        
        # create new ship
        if num_of_ships_around == 0:
            comp_field[string][column] = self
            if not is_bot:
                user_field[string][column] = "*"

        # continue ship
        elif num_of_ships_around == 1:

            # check continue of ship
            for i in (1, -1):
                try:
                    column_cell = comp_field[string][column + i] # there are change only column
                    string_cell = comp_field[string + i][column] # there are change only string
                except:
                    continue

                if isinstance(column_cell, Ship):
                    comp_field[string][column] = column_cell

                    if (column_cell.length + 1 == comp_field[string].count(column_cell)) and (column_cell.length + 1 <= 4):
                        column_cell.length += 1
                        if not is_bot:
                            user_field[string][column] = "*"
                    else:
                        comp_field[string][column] = "-"


                if isinstance(string_cell, Ship):
                    num_of_ships_around += 1

        return False

ship1 = Ship()
ship2 = Ship()
ship3 = Ship()
ship4 = Ship()
ship5 = Ship()
ship6 = Ship()

ship1.put_ship(comp_field, user_field, (3, 4))
ship2.put_ship(comp_field, user_field, (3, 5))
ship3.put_ship(comp_field, user_field, (3, 6))
ship4.put_ship(comp_field, user_field, (3, 7))

ship6.put_ship(comp_field, user_field, (4, 6))
ship5.put_ship(comp_field, user_field, (5, 6))



print_field(user_field)

