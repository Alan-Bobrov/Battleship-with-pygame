import pygame as pg
from random import randint

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
                        return True, True, (iy, jx)
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
                    list_live_ships.append(self.field[i[0]][i[1]])
                elif self.field[i[1]][i[0]].status == "hit":
                    list_hit_ships.append(self.field[i[0]][i[1]])

        if len(list_hit_ships) == 0 and len(list_live_ships) == 0:
            for i in list_coords_2:
                self.field[i[1]][i[0]].status = "skip"
                self.field[i[1]][i[0]].images.append(pg.image.load("images/Skip.png"))
                self.live_ships -= 1
        

class Place:
    def __init__(self, X, Y) -> None:
        self.images = []
        self.status = "free_place"
        self.X = X
        self.Y = Y

class Skip:
    def __init__(self) -> None:
        self.image = "images/Skip.png"

class Hit:
    def __init__(self) -> None:
        self.image = "images/Hit.png"

#field = Field(110, 476)
#skip = Skip()
#hit = Hit()


#FieldImg = pg.image.load(field.image)
#SkipImg = pg.image.load(skip.image)
#HitImg = pg.image.load(hit.image)