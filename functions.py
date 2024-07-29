def new_ship():
    pass
# хуйня
def test_all_cells():
    pass
# хуйня
def player_play():
    pass
# хуйня

def bot_play():
    # хуйня
    pass

def test_death():
    # хуйня
    pass
  
def play():
    # хуйня
    pass

def fire_pg(screen, x, y, x_coords, y_coords, Img):
    for iy in range(10):
        for jx in range(10):
            if (x_coords[jx][0] <= x <= x_coords[jx][1]) and (y_coords[iy][0] <= y <= y_coords[iy][1]):
                screen.blit(Img, (x_coords[jx][0], y_coords[iy][0]))