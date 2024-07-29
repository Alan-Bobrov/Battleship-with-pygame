import pygame as pg

class Field:
    def __init__(self, live_ships=9) -> None:
        self.image = "images/Field.png"
        self.live_ships = live_ships

    def copying(self, field_copy, copyable_status):
        pass

field = Field()

FieldImg = pg.image.load(field.image)
