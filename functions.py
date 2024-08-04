from images import *
import json

def new_ship():
    pass

def test_all_cells():
    pass

def player_play():
    pass

def test_death():
    pass
  
def play():
    pass

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

def clear_field(screen):
    screen.blit(FieldImg, (0, 0))
    return_num_ships()

def SetClearButton(screen, is_clear):
    screen.blit(ClearImg, (81, 55))
    is_clear = True
    return is_clear

