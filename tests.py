from random import choice

class Field:
    def __init__(self, status="free_place", live_ships = 9, given_field = None) -> None:
        if given_field == None:
            field = []
            for _ in range(1, 11):
                field.append([status, status, status, status, status, status, status, status, status, status])
            self.field = field
        else:
            self.field = given_field














