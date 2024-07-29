import pygame as pg

class Field:
    def __init__(self) -> None:
        self.image = "images/Field.png"

field = Field()

FieldImg = pg.image.load(field.image)
