import pygame as pg
from loads.images import *
from loads.settings import *
import json

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

def print_field(field, is_change=False):
    if is_change:
        for i in field:
            for j in i:
                if not isinstance(j, str):
                    print("o", end="")
                else:
                    print(j, end="")
            print()
    else:
        for i in range(len(field)):
            print(*field[i])

def update_num_of_ships(cell):
    with open("num_of_ships.json", "r", encoding="utf-8") as num_of_ships:
        num_of_ships = json.load(num_of_ships)

        # if ships with such length is over
        if num_of_ships[f"{cell.length}"] < 1:
            return False
            
        num_of_ships[f"{cell.length - 1}"] += 1
        num_of_ships[f"{cell.length}"] -= 1

        with open("num_of_ships.json", "w", encoding="utf-8") as file:
            json.dump(num_of_ships, file, indent=4)
            
    return True

def PlaySound(SoundName: str):
    SoundName = SoundName.strip()

    if IsClasic:
        full_name = f"sounds/{Language}/Classic/{SoundName}.wav"
    else:
        if IsSwears:
            full_name = f"sounds/{Language}/Funny/Swears/{SoundName}.wav"
        else:
            full_name = f"sounds/{Language}/Funny/Default/{SoundName}.wav"

    sound = pg.mixer.Sound(full_name)
    sound.play()

def PlayMusic(MusicName: str):
    MusicName = MusicName.strip()
    full_name = "music/" + MusicName + ".mp3"
    pg.mixer.music.load(full_name)
    pg.mixer.music.set_volume(0.2)
    pg.mixer.music.play(loops=1, fade_ms=500)

def change_coords(x, y, first_x, first_y): # 889 577
    count = 0
    new_x, new_y = 0, 0

    for i in range(10):
        num = first_x + (32 * i)
        if num <= x < num + 32:
            new_x = i
            count += 1
            break

    for j in range(10):
        num = first_y + (32 * j)
        if num <= y < num + 32:
            new_y = j
            count += 1
            break
                        
    if count == 2:
        return True, new_x, new_y
    else:
        return False, new_x, new_y

def restart_game(screen):
    screen.blit(FieldImg, (0, 0))
    return_num_ships()

def clear_field(screen):
    screen.blit(FieldImg, (0, 0))
    return_num_ships()

def SetRestartButton(screen):
    '''
    Function put button for restart game
    is_again - is it end of rhe game
    '''
    screen.blit(RestartImg, (0, 0))