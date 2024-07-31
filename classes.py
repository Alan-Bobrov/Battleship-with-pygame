import pygame as pg
from random import randint

class Field:
    def __init__(self, first_X, first_Y, live_ships=9) -> None: #110 476 - first field and 598 476 - second
        self.image = "images/Field.png"
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
            if self.fire_pg(X, Y):
                break
    
    def bot_do_ships(self): #эта функция расстановления ботом кораблей, она врененная
        while True:
            X = randint(0, 9)
            Y = randint(0, 9)
            if self.field[Y][X].status == "free_place":
                self.field[Y][X].status = "part_ship"
                self.field[Y][X].images.append(pg.image.load("images/OneDeckShip.png"))
                break
    
    def fire_pg(self, x, y) -> bool:
        for iy in range(10):
            for jx in range(10):
                X = self.field[iy][jx].X
                Y = self.field[iy][jx].Y
                if (X <= x < X + 32) and (Y <= y < Y + 32):
                    if self.field[iy][jx].status == "free_place":
                        self.field[iy][jx].status = "skip"
                        self.field[iy][jx].images.append(pg.image.load("images/Skip.png"))
                        return True
                    elif self.field[iy][jx].status == "part_ship":
                        self.field[iy][jx].status = "hit"
                        self.field[iy][jx].images.append(pg.image.load("images/Hit.png"))
                        return True
        return False


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

field = Field(110, 476)
skip = Skip()
hit = Hit()


FieldImg = pg.image.load(field.image)
SkipImg = pg.image.load(skip.image)
HitImg = pg.image.load(hit.image)