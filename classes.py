import pygame as pg
from random import randint
from functions import *
from images import *
import json

class Field:
    def __init__(self, first_X, first_Y, live_ships=9) -> None: #110 476 - first field and 598 476 - second
        self.live_ships = live_ships
        self.field = [[Place(first_X + j * 32, first_Y + i * 32) for j in range(10)] for i in range(10)]

    def pr_all(self, screen, print_ships=False):
        status_list = ["skip", "hit"]
        if print_ships:
            status_list.append("part_ship")
        
        for i in self.field:
            for j in i:
                if j.status in status_list:
                    for image in j.images:
                        if image == ShipStartImg:
                            screen.blit(image, (j.X, j.Y - 2))
                        elif image == ShipEndImg: 
                            screen.blit(image, (j.X, j.Y + 2))
                        elif len(j.images) == 2 and j.images[1] == "end":
                                screen.blit(j.images[0], (j.X + 2, j.Y))
                        elif len(j.images) == 2 and j.images[1] == "start":
                            screen.blit(j.images[0], (j.X - 2, j.Y))
                        else:
                            screen.blit(image, (j.X, j.Y))
    
    def bot_play(self):
        while True:
            X = randint(0, 9) * 32 + 110
            Y = randint(0, 9) * 32 + 476
            end = self.fire_pg(X, Y)
            if end[0]:
                if end[1]:
                    self.death(end[2][0], end[2][1])
                break
    
    def do_ships(self, coords, num_of_ships, bot, *args): 
        if len(args) == 0:
            comp_field = create_field()
        else:
            comp_field = args[0]
        if bot:
            return_num_ships()
        num_of_ships = ship_gen(comp_field, num_of_ships, bot, coords)
        for i in range(len(comp_field)):
            for j in range(len(comp_field[0])):
                if type(comp_field[i][j]) == Ship and self.field[i][j].status != "part_ship":
                    self.field[i][j].status = "part_ship"
                    self.field[i][j].images.append(ShipContinueImg)
        
        return num_of_ships

    def normal_ships_image(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].status == "part_ship":
                    up, down, right, left = Place(0, 0), Place(0, 0), Place(0, 0), Place(0, 0)
                    if i - 1 >= 0:
                        up = self.field[i - 1][j]
                    if i + 1 <= 9:
                        down = self.field[i + 1][j]
                    if j + 1 <= 9:
                        right = self.field[i][j + 1]
                    if j - 1 >= 0:
                        left = self.field[i][j - 1]
                    
                    if up.status == "part_ship" and down.status == "part_ship":
                        self.field[i][j].images = [ShipContinueImg]
                    elif up.status == "part_ship" and down.status != "part_ship":
                        self.field[i][j].images = [ShipStartImg]
                    elif up.status != "part_ship" and down.status == "part_ship":
                        self.field[i][j].images = [ShipEndImg]
                    elif right.status == "part_ship" and left.status == "part_ship":
                        self.field[i][j].images = [pg.transform.rotate(ShipContinueImg, 90.0)]
                    elif right.status == "part_ship" and left.status != "part_ship":
                        self.field[i][j].images = [pg.transform.rotate(ShipEndImg, 90.0), "end"]
                    elif right.status != "part_ship" and left.status == "part_ship":
                        self.field[i][j].images = [pg.transform.rotate(ShipStartImg, 90.0), "start"]
                    else:
                        self.field[i][j].images = [OneDeckShipImg]
            
    def fire_pg(self, x, y) -> tuple:
        for iy in range(10):
            for jx in range(10):
                X = self.field[iy][jx].X
                Y = self.field[iy][jx].Y
                if (X <= x < X + 32) and (Y <= y < Y + 32):
                    if self.field[iy][jx].status == "free_place":
                        self.field[iy][jx].status = "skip"
                        self.field[iy][jx].images.append(SkipImg)
                        return True, False
                    elif self.field[iy][jx].status == "part_ship":
                        self.field[iy][jx].status = "hit"
                        self.field[iy][jx].images.append(HitImg)
                        self.death(jx, iy)
                        return True, True, (jx, iy)
        return False, False

    def death(self, x, y):
        list_coords = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        list_coords_2 = []
        list_live_ships = []
        list_hit_ships = []
        for i in list_coords:
            if 0 <= i[0] <= 9 and 0 <= i[1] <= 9:
                list_coords_2.append(i)
                if self.field[i[1]][i[0]].status == "part_ship":
                    list_live_ships.append(self.field[i[1]][i[0]])
                elif self.field[i[1]][i[0]].status == "hit":
                    list_hit_ships.append(self.field[i[1]][i[0]])

        if len(list_hit_ships) == 0 and len(list_live_ships) == 0:
            for i in list_coords_2:
                self.field[i[1]][i[0]].status = "skip"
                self.field[i[1]][i[0]].images.append(pg.image.load("images/Skip.png"))
                self.live_ships -= 1

class Ship:
    def __init__(self) -> None:
        self.length = 1
        self.hp = 1
        self.direction = None # tuple like (-1, 0)
        self.start_coords = None # tuple like (0, 0)

    def put_ship(self, comp_field, coords) -> tuple:
    
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
                    return False, None
                num_of_ships["1"] -= 1
                self.start_coords = coords
                with open("num_of_ships.json", "w", encoding="utf-8") as file1:
                    json.dump(num_of_ships, file1, indent=4)
            return True, "new"

        # continue ship
        elif num_of_ships_around == 1:

            # check continue of ship
            for i in (1, -1):

                # we will check cells around coords
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
                        column_cell.hp += 1
                        if not update_num_of_ships(column_cell):
                            column_cell.length -= 1
                            column_cell.hp -= 1
                            comp_field[string][column] = "-"
                            return False, None
                        column_cell.direction = (0, i)
                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    return True, None

                # if vertical ship
                if isinstance(string_cell, Ship):
                    column_values = list()
                    for _ in range(10):
                        column_values.append(comp_field[_][column])
                    
                    comp_field[string][column] = string_cell
                    if (string_cell.length == column_values.count(string_cell)) and (string_cell.length + 1 <= 4):
                        string_cell.length += 1
                        string_cell.hp += 1
                        if not update_num_of_ships(string_cell):
                            string_cell.length -= 1
                            string_cell.hp -= 1
                            comp_field[string][column] = "-"
                        string_cell.direction = (i, 0)
                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    return True, None

        return False, None

    def create_ship(comp_field, coords):
        ship = Ship()
        result = ship.put_ship(comp_field, coords)
        return result
    
    def death(self, comp_field, coords):
        string, col = coords
        fired_cell = comp_field[string][col]

        # death for one-deck ship
        if fired_cell.length == 1:
            for i in (1, -1):
                for j in (1, -1):
                    if (0 <= string + i <= 9) and (0 <= col + j <= 9):
                        comp_field[string + i][col + j] = "*"
                if (0 <= col + i <= 9):
                    comp_field[string][col + i] = "*"
                
                if (0 <= string + i <= 9):
                    comp_field[string + i][col] = "*"
            return None

        start_string = fired_cell.start_coords[0]
        start_col = fired_cell.start_coords[1]

        str_dire = fired_cell.direction[0]
        col_dire = fired_cell.direction[1]

        var = (fired_cell.length - 1, -1, fired_cell.length - 1)

        # vertical ship death
        if str_dire:

            # sides of ship 
            for i in range(var[str_dire], var[str_dire - 1], str_dire):
                if col + 1 <= 9:
                    comp_field[start_string + i][start_col + 1] = "*"

                if col - 1 >= 0:
                    comp_field[start_string + i][start_col - 1] = "*"
            
            # top and end of ship
            # idk why '+' -------\/
            if 0 <= start_string + str_dire <= 9:
                comp_field[start_string + str_dire][start_col] = "*"

            if 0 <= start_string + fired_cell.length <= 9:
                comp_field[start_string + fired_cell.length][start_col] = "*"
            
            for i in (-1, fired_cell.length):
                for j in (-1, 1):
                    if (0 <= (start_string - (i * str_dire)) <= 9) and (0 <= (start_col + j) <= 9):
                        comp_field[start_string - (i * str_dire)][start_col + j] = "*"

            
        
        elif col_dire:

            # sides of ship
            for i in range(var[col_dire], var[col_dire - 1], col_dire):
                if string + 1 <= 9:
                    comp_field[start_string + 1][start_col + i] = "*"
                
                if string - 1 >= 0:
                    comp_field[start_string - 1][start_col + i] = "*"

            if 0 <= start_col + col_dire <= 9:
                comp_field[start_string][start_col + col_dire] = "*"
            
            if 0 <= start_col + fired_cell.length <= 9:
                comp_field[start_string][start_col + fired_cell.length] = "*"
        




    def fire(self, comp_field, coords):
        string, col = coords
        fired_cell = comp_field[string][col]

        if isinstance(fired_cell, Ship):
            if fired_cell.hp >= 1:
                fired_cell.hp -= 1

                if fired_cell.hp <= 0:
                    fired_cell.death(comp_field, coords)
        
        comp_field[string][col] = "o"



class Place:
    def __init__(self, X, Y) -> None:
        self.images = []
        self.status = "free_place"
        self.X = X
        self.Y = Y

#Do not delete!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def ship_gen(comp_field, num_of_ships, bot, coords):
        if bot:
            while num_of_ships < 10:
                coords = (randint(0, 9), randint(0, 9))
                result = Ship.create_ship(comp_field, coords)
                if result[1] == "new":
                    num_of_ships += 1      

            return num_of_ships

        else:
            result = Ship.create_ship(comp_field, coords)
            if result[1] == "new":
                num_of_ships += 1        
        return num_of_ships

# class Skip:
#     def __init__(self) -> None:
#         self.image = "images/Skip.png"

# class Hit:
#     def __init__(self) -> None:
#         self.image = "images/Hit.png"

#field = Field(110, 476)
#skip = Skip()
#hit = Hit()


#FieldImg = pg.image.load(field.image)
#SkipImg = pg.image.load(skip.image)
#HitImg = pg.image.load(hit.image)
