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

        self.live_ships = live_ships
    
    def copying(self, field_copy, copyable_status):
        pass

class Ship:
    def __init__(self, Y, X, len_ship, direction) -> None:
        self.Y = Y.upper()
        self.X = X
        self.len_ship = len_ship
        if len_ship == 1:
            self.direction = "one"
        else:
            self.direction = direction.lower()

    def all_places(self):
        pass

    def test_near_ship(self):
        pass
    
    def test_free_place(self):
        pass

    def death(self):
        pass
            
def new_ship():
    pass

def test_all_cells():
    pass

def player_play():
    pass

def bot_play():
    pass

def test_death():
    pass
  
def play():
    pass















