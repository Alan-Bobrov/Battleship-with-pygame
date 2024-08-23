from random import randint
from functions import *
from images import *
import json

class Field:
    def __init__(self, first_X, first_Y, live_ships=9) -> None: #108 474 - first field and 596 474 - second
        self.live_ships = live_ships
        self.field = [[Place(first_X + j * 32, first_Y + i * 32) for j in range(10)] for i in range(10)]

    def pr_all(self, screen, print_ships=False):
        tuple_ships_images = (OneDeckShipImg, ShipContinueImg, ShipEndImg, ShipStartImg, TransformShipContinueImg, TransformShipEndImg, TransformShipStartImg)

        if print_ships:
            for i in self.field:
                for j in i:
                    for image in j.images:
                        screen.blit(image, (j.X, j.Y))
        else:
            for i in self.field:
                for j in i:
                    for image in j.images:
                        if image in tuple_ships_images:
                            continue    
                        else:
                            screen.blit(image, (j.X, j.Y))
    
    def do_ships(self, coords, num_of_ships, bot, comp_field): 
        if bot:
            return_num_ships()
        num_of_ships = Ship.ship_gen(Ship, comp_field, 0, bot, coords)
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
                        self.field[i][j].images[0] = ShipContinueImg
                    elif up.status == "part_ship" and down.status != "part_ship":
                        self.field[i][j].images[0] = ShipStartImg
                    elif up.status != "part_ship" and down.status == "part_ship":
                        self.field[i][j].images[0] = ShipEndImg
                    elif right.status == "part_ship" and left.status == "part_ship":
                        self.field[i][j].images[0] = TransformShipContinueImg
                    elif right.status == "part_ship" and left.status != "part_ship":
                        self.field[i][j].images[0] = TransformShipEndImg
                    elif right.status != "part_ship" and left.status == "part_ship":
                        self.field[i][j].images[0] = TransformShipStartImg
                    else:
                        self.field[i][j].images[0] = OneDeckShipImg
            
    def synchronize(self, x, y, comp_field=None):
        if comp_field == None:
            if self.field[y][x].status == "free_place":
                self.field[y][x].status = "skip"
                self.field[y][x].images.append(SkipImg)
            elif self.field[y][x].status == "part_ship":
                self.field[y][x].status = "hit"
                self.field[y][x].images.append(HitImg)
        else:
            for i in range(10):
                for j in range(10):
                    if comp_field[i][j] == "*" and self.field[i][j].status != "skip":
                        self.field[i][j].status = "skip"
                        self.field[i][j].images.append(SkipImg)

class Ship:
    def __init__(self) -> None:
        self.length = 1
        self.hp = 1
        self.direction = None # tuple like (-1, 0)
        self.start_coords = None # tuple like (0, 0)

    def put_ship(self, comp_field, coords) -> tuple:
        '''
        return status of ship create (is it was created)
        if ship was created return is it new ship or continueof another ship 
        '''
    
        string, column = coords

        # is valid coords 
        if isinstance(string, int) and isinstance(column, int): # is it nums (not string and other)

            # is coords inside field and coords cell is free
            if (string <= -1 or string >= 10) or (column <= -1 or column >= 10) or comp_field[string][column] != "-":
                return False, None
        else:
            return False, None
        
        # check corners of ship
        for str_chng in (1, -1): 
            for col_chng in (1, -1):
                if (0 <= string + str_chng <= 9) and (0 <= column + col_chng <= 9):
                    if isinstance(comp_field[string + str_chng][column + col_chng], Ship):
                        return False, None

        num_of_ships_around = 0

        # check num of ships around coords
        '''
                *
              * o *
                *
        o - coords
        * - checking
        '''
        for i in (1, -1):
            
            # check cells sround ship
            try:
                if column + i <= -1:
                    raise IndexError
                column_cell = comp_field[string][column + i] # there are change only column
            except:
                column_cell = comp_field[string][column]

            try:
                if string + i <= -1:
                    raise IndexError
                string_cell = comp_field[string + i][column] # there are change only string
            except:
                string_cell = comp_field[string][column]

            # check column cell and srtring cell
            if isinstance(column_cell, Ship):
                num_of_ships_around += 1

            if isinstance(string_cell, Ship):
                num_of_ships_around += 1

        # create new ship
        if num_of_ships_around == 0:
            comp_field[string][column] = self

            with open("num_of_ships.json", "r", encoding="utf-8") as file:
                num_of_ships = json.load(file)

                # if one-deck ships is over
                if num_of_ships["1"] <= 0:
                    comp_field[string][column] = "-"
                    return False, None
                
                num_of_ships["1"] -= 1
                self.start_coords = coords

                # update num_of_ships.json
                with open("num_of_ships.json", "w", encoding="utf-8") as file1:
                    json.dump(num_of_ships, file1, indent=4)

            return True, "new"

        # continue ship
        elif num_of_ships_around == 1:

            # check continue of ship
            for i in (1, -1):

                # we will check cells around coords
                try:
                    if column + i <= -1:
                        raise IndexError
                    column_cell = comp_field[string][column + i] # there are change only column
                except:
                    column_cell = comp_field[string][column]

                try:
                    if string + i <= -1:
                        raise IndexError
                    string_cell = comp_field[string + i][column] # there are change only string
                except:
                    string_cell = comp_field[string][column]

                
                # if horizontal ship
                if isinstance(column_cell, Ship):
                    comp_field[string][column] = column_cell

                    if (column_cell.length + 1 == comp_field[string].count(column_cell)) and (column_cell.length + 1 <= 4):
                        column_cell.length += 1
                        column_cell.hp += 1

                        # is ships with such len is accepted
                        if not update_num_of_ships(column_cell):
                            column_cell.length -= 1
                            column_cell.hp -= 1
                            comp_field[string][column] = "-"
                            return False, None
                        
                        column_cell.direction = (0, 1)

                        if (column < column_cell.start_coords[1]):
                            column_cell.start_coords = (string, column)

                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    
                    return True, None

                # if vertical ship
                elif isinstance(string_cell, Ship):

                    # list with all values in column
                    column_values = list()
                    for _ in range(10):
                        column_values.append(comp_field[_][column])
                    
                    comp_field[string][column] = string_cell

                    if (string_cell.length == column_values.count(string_cell)) and (string_cell.length + 1 <= 4):

                        string_cell.length += 1
                        string_cell.hp += 1

                        # is ships with such len is accepted
                        if not update_num_of_ships(string_cell):
                            string_cell.length -= 1
                            string_cell.hp -= 1
                            comp_field[string][column] = "-"
                            return False, None

                        string_cell.direction = (1, 0)

                        if (string < string_cell.start_coords[0]):
                            string_cell.start_coords = (string, column)

                    else:
                        comp_field[string][column] = "-"
                        return False, None
                    
                    return True, None

        return False, None
    
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

        # vertical ship death
        if str_dire:

            # sides of ship 
            for i in range(fired_cell.length): # 0, 1
                if start_col + 1 <= 9:
                    comp_field[start_string + i][start_col + 1] = "*"

                if start_col - 1 >= 0:
                    comp_field[start_string + i][start_col - 1] = "*"
            
            # top and end of ship
            if 0 <= start_string - 1 <= 9:
                comp_field[start_string - 1][start_col] = "*"

            if 0 <= start_string + fired_cell.length <= 9:
                comp_field[start_string + fired_cell.length][start_col] = "*"
            
            # corners of ship
            for i in (-1, fired_cell.length):
                for j in (-1, 1):
                    if (0 <= (start_string + i) <= 9) and (0 <= (start_col + j) <= 9):
                        comp_field[start_string + i][start_col + j] = "*"

        # horizontal ship death
        elif col_dire:

            # sides of ship
            for i in range(fired_cell.length): # 0, 1
                if start_string + 1 <= 9:
                    comp_field[start_string + 1][start_col + i] = "*"
                
                if start_string - 1 >= 0:
                    comp_field[start_string - 1][start_col + i] = "*"

            # top and end of ship
            if 0 <= start_col - 1 <= 9:
                comp_field[start_string][start_col - 1] = "*"
            
            if 0 <= start_col + fired_cell.length <= 9:
                comp_field[start_string][start_col + fired_cell.length] = "*"
            
            # corners of ship
            for i in (-1, fired_cell.length):
                for j in (-1, 1):
                    if (0 <= (start_string + j) <= 9) and (0 <= (start_col + i) <= 9):
                        comp_field[start_string + j][start_col + i] = "*"  

    def fire(self, comp_field, coords) -> tuple: # tuple - (is hit, Death/Hit/None)
        string, col = coords # 4 9
        fired_cell = comp_field[string][col]

        if isinstance(fired_cell, Ship):
            if fired_cell.hp >= 1:
                fired_cell.hp -= 1

                if fired_cell.hp <= 0:
                    fired_cell.death(comp_field, coords)
                    comp_field[string][col] = "o"
                    return True, "Death"
                
                comp_field[string][col] = "o"
                return True, "Hit"
        
        comp_field[string][col] = "o"

        return False, None
    
    def ship_gen(self, comp_field, num_of_ships):
        '''
        function randomly put ships on the field
        '''
<<<<<<< HEAD
        if bot:
            num_of_errors = 0
            while num_of_ships <= 10:
=======
        # num_of_ships = 0
        num_of_errors = 0
        while num_of_ships <= 10:
>>>>>>> a740cc1b57e8d484dc512f004441b837e52141dc

            if num_of_errors >= 300:
                num_of_errors = 0
                num_of_ships = 0
                comp_field = create_field()
                return_num_ships()
                
            ship = Ship()
            result = ship.put_ship(comp_field, (randint(0, 9), randint(0, 9)))

            if not result[0]:
                num_of_errors += 1
                
<<<<<<< HEAD
                if result[1] == "new":
                    num_of_ships += 1

            return num_of_ships


        else:
            S = Ship()
            result = S.put_ship(comp_field, coords)
            if result[1] == "new":
                num_of_ships += 1   
=======
            if result[1] == "new":
                num_of_ships += 1
>>>>>>> a740cc1b57e8d484dc512f004441b837e52141dc

        return num_of_ships

class Place:
    def __init__(self, X, Y) -> None:
        self.images = []
        self.status = "free_place"
        self.X = X
        self.Y = Y

class Bot:
    def __init__(self) -> None:
        self.last_hits = list() # (((2, 3), "Death"), ((7, 9), "Hit")))
        self.changes = tuple()  # (1, 0)

    def cell_selection(self, comp_field) -> tuple: # return (status of fire (is hit)) and (coords of fire) 
        
        is_coord = False # is coords was created 

        # if hit >= 2 time in row
        if len(self.last_hits) >= 2:
            col_change = self.changes[1]
            str_change = self.changes[0]

            # if horizontal ship
            if col_change:

                # is valid coords
                if self.last_hits[0][0][1] - 1 >= 0:
                    fire_cell = comp_field[self.last_hits[0][0][0]][self.last_hits[0][0][1] - 1]
                    if isinstance(fire_cell, Ship) or fire_cell == "-":
                        coords = (self.last_hits[0][0][0], self.last_hits[0][0][1] - 1)
                        is_coord = True

                if (self.last_hits[-1][0][1] + 1 <= 9) and not is_coord:
                    fire_cell = comp_field[self.last_hits[-1][0][0]][self.last_hits[-1][0][1] + 1]
                    if isinstance(fire_cell, Ship) or fire_cell == "-":
                        coords = (self.last_hits[-1][0][0], self.last_hits[-1][0][1] + 1)
                    
                    else:
                        coords = coords = randint(0, 9), randint(0, 9)
            
            # if vertical ship
            elif str_change:

                # is valid coords
                if self.last_hits[0][0][0] - 1 >= 0:
                    fire_cell = comp_field[self.last_hits[0][0][0] - 1][self.last_hits[0][0][1]]
                    if isinstance(fire_cell, Ship) or fire_cell == "-":
                        coords = (self.last_hits[0][0][0] - 1, self.last_hits[0][0][1])
                        is_coord = True

                if (self.last_hits[-1][0][0] + 1 <= 9) and not is_coord:
                    fire_cell = comp_field[self.last_hits[-1][0][0] + 1][self.last_hits[-1][0][1]]
                    if isinstance(fire_cell, Ship) or fire_cell == "-":
                        coords = (self.last_hits[-1][0][0] + 1, self.last_hits[-1][0][1])
                    
                    else:
                        coords = coords = randint(0, 9), randint(0, 9)

        # if hit only 1 time
        elif len(self.last_hits) == 1:

            # choose random cell around last hit cell
            for i in (-1, 1):
                if 0 <= self.last_hits[0][0][0] + i <= 9:
                    fire_cell = comp_field[self.last_hits[0][0][0] + i][self.last_hits[0][0][1]]
                    if fire_cell == "-" or isinstance(fire_cell, Ship):
                        coords = (self.last_hits[0][0][0] + i, self.last_hits[0][0][1])
                        break

                if 0 <= self.last_hits[0][0][1] + i <= 9:
                    fire_cell = comp_field[self.last_hits[0][0][0]][self.last_hits[0][0][1] + i]
                    if fire_cell == "-" or isinstance(fire_cell, Ship):
                        coords = (self.last_hits[0][0][0], self.last_hits[0][0][1] + i)
                        break

        # if no hit 
        else:
            while True:
                coords = randint(0, 9), randint(0, 9)
                fire_cell = comp_field[coords[0]][coords[1]]
                if fire_cell == "-" or isinstance(fire_cell, Ship):
                    break

        result = Ship.fire(Ship, comp_field, coords)

        # get result of fire
        is_hit = result[0]
        result_of_fire = result[1]
        self.last_fire = coords

        if is_hit:

            # if ship destroyed
            if result_of_fire == "Death":
                self.last_hits = list()
                self.changes = tuple()
                return is_hit, coords
            
            self.last_hits.insert(0, (coords, result_of_fire))
            self.last_hits.sort()

            # change direction of ship
            if len(self.last_hits) >= 2:
                first_str, first_col = self.last_hits[0][0]
                second_str, second_col = self.last_hits[1][0]

                self.changes = (abs(first_str - second_str), abs(first_col - second_col))

        return is_hit, coords
