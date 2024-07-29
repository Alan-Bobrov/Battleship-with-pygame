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

def fire_pg(screen, x, y, x_coords, y_coords, Img):
    for iy in range(10):
        for jx in range(10):
            if (x_coords[jx][0] <= x <= x_coords[jx][1]) and (y_coords[iy][0] <= y <= y_coords[iy][1]):
                screen.blit(Img, (x_coords[jx][0], y_coords[iy][0]))