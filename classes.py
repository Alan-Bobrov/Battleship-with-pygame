import pygame as pg

class Field:
    def __init__(self, live_ships=9, first_X, first_Y) -> None: #110 476 - first field and 598 476 - second
        self.image = "images/Field.png"
        self.live_ships = live_ships
        self.field = [[Place(first_X + j * 32, first_Y + i * 32) for j in range(10)] for i in range(10)]

    def copying(self, field_copy, copyable_status):
        pass

class Place:
    def __init__(self, X, Y) -> None:
        self.image = None
        self.status = "free_place"
        self.X = X
        self.Y = Y

field = Field()

FieldImg = pg.image.load(field.image)
