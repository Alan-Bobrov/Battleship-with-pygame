def create_field(space_symbol="-"):
    field = [[space_symbol for _ in range(10)] for i in range(10)]
    return field

def print_field(field):
    for i in range(len(field)):
        print(*field[i])

def put_ship(field, coords):
    num_of_ships_around = 0
    string, column = coords
    for i in (1, -1):
        if field[string][column + i] == "*":
            num_of_ships_around += 1
    for i in (1, -1):
        if field[string + i][column] == "*":
            num_of_ships_around += 1 

    if num_of_ships_around <= 1:
        field[string][column] = "*"
    return num_of_ships_around

field = create_field()
a = put_ship(field, (4, 5))
c = put_ship(field, (4, 7))
b = put_ship(field, (4, 6))
print_field(field)
print(a)
print(c)
print(b)