import pygame as pg
from random import randint
from functions import *

class Field:
    def __init__(self, first_X, first_Y, live_ships=9) -> None: #110 476 - first field and 598 476 - second
        self.live_ships = live_ships
        self.field = [[Place(first_X + j * 32, first_Y + i * 32) for j in range(10)] for i in range(10)]

    def copying(self, field_copy, copyable_status):
        pass

    def pr_all(self, screen, print_ships=False):
        status_list = ["skip", "hit"]
        if print_ships:
            status_list.append("part_ship")
        
        for i in self.field:
            for j in i:
                if j.status in status_list:
                    for image in j.images:
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
    
    def bot_do_ships(self): #эта функция расстановления ботом кораблей, она врененная
        while True:
            X = randint(0, 9)
            Y = randint(0, 9)
            if self.field[Y][X].status == "free_place":
                self.field[Y][X].status = "part_ship"
                self.field[Y][X].images.append(pg.image.load("images/OneDeckShip.png"))
                break
    
    def fire_pg(self, x, y) -> tuple:
        for iy in range(10):
            for jx in range(10):
                X = self.field[iy][jx].X
                Y = self.field[iy][jx].Y
                if (X <= x < X + 32) and (Y <= y < Y + 32):
                    if self.field[iy][jx].status == "free_place":
                        self.field[iy][jx].status = "skip"
                        self.field[iy][jx].images.append(pg.image.load("images/Skip.png"))
                        return True, False
                    elif self.field[iy][jx].status == "part_ship":
                        self.field[iy][jx].status = "hit"
                        self.field[iy][jx].images.append(pg.image.load("images/Hit.png"))
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
                    print(9)
                    return False, None
                num_of_ships["1"] -= 1
                with open("num_of_ships.json", "w", encoding="utf-8") as file1:
                    json.dump(num_of_ships, file1, indent=4)
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
                        if not update_num_of_ships(column_cell):
                            column_cell.length -= 1
                            comp_field[string][column] = "-"
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
                        if not update_num_of_ships(string_cell):
                            string_cell.length -= 1
                            comp_field[string][column] = "-"
                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    return True, ("Down" if i == 1 else "Up")

        return False, None
        

class Place:
    def __init__(self, X, Y) -> None:
        self.images = []
        self.status = "free_place"
        self.X = X
        self.Y = Y

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