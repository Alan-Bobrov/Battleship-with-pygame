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
        self.num_of_accepted_ships = {
            4: 1,
            3: 2,
            2: 3,
            1: 4
        }

    def put_ship(self, comp_field, user_field, coords):
        string, column = coords

        # check corners of ship
        for i in (1, -1):
            for j in (1, -1):
                if isinstance(comp_field[string + i][column + j], Ship):
                    return False
            
        num_of_ships_around = 0

        # check num of ships around coords
        for i in (1, -1):
            if isinstance(comp_field[string][column + i], Ship):
                num_of_ships_around += 1

            if isinstance(comp_field[string + i][column], Ship):
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
ship2.put_ship(comp_field, user_field, (3, 6))
ship3.put_ship(comp_field, user_field, (3, 5))

print_field(user_field)

