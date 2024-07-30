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
        self.num_of_accepted_ships = {
            4: 1,
            3: 2,
            2: 3,
            1: 4
        }

    def put_ship(self, comp_field, user_field, coords, is_bot=False):
        string, column = coords

        # check corners of ship
        for i in (1, -1):
            for j in (1, -1):
                if isinstance(comp_field[string + i][column + j], Ship):
                    return False
            
        num_of_ships_around = 0

        # check num of ships around coords
        for i in (1, -1):
            column_cell = comp_field[string][column + i] # there are change only column
            string_cell = comp_field[string + i][column] # there are change only string

            if isinstance(column_cell, Ship):
                comp_field[string][column] = column_cell
                if column_cell.length + 1 != comp_field[string].count(column_cell):
                    comp_field[string][column] = "-"
                    return False
                column_cell.length += 1
                num_of_ships_around += 1

            if isinstance(string_cell, Ship):
                num_of_ships_around += 1
        
        # if coords - continue of the ship or it is a one-deck ship
        if num_of_ships_around <= 1:
            comp_field[string][column] = self
            user_field[string][column] = "*"
            return True

        return False

ship1 = Ship()
ship2 = Ship()
ship3 = Ship()

ship1.put_ship(comp_field, user_field, (3, 4))
ship2.put_ship(comp_field, user_field, (3, 5))
ship3.put_ship(comp_field, user_field, (2, 6))


print_field(user_field)

