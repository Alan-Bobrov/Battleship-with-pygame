
# automaticly pip install pygame
try:
    import pygame as pg
except:
    from subprocess import check_call
    from sys import executable
    check_call([executable, "-m", "pip", "install", "pygame"])

# our files
from classes import *
from functions import *
from loads.images import *
from loads.settings import *

from time import sleep
from threading import Thread
from loads.settings import *

def BattleShip():
    def game():
        pg.init()

        player_field = Field(108, 474)
        bot_field = Field(596, 474)

        # bot arranges ships
        bot_comp_field = create_field()
        bot_field.do_ships(None, 0, True, bot_comp_field)
        bot_field.normal_ships_image()
        return_num_ships()

        screen = pg.display.set_mode((1024, 900))
        screen.fill((255, 255, 255))

        is_game = True
        num_of_ships = 0 # number of ships the player has placed
        do_ship = True # is the player currently placing ships
        player_comp_field = create_field()
        player_ship_count = 0
        bot_ship_count = 0
        first_move = False
        can_go = True
        bot_ob = Bot()
        bot_move = False
        changed = False
        players_attack_result = (True, )

        while is_game:

            # field print
            screen.blit(FieldImg, (0, 0))
            player_field.pr_all(screen, print_ships=ShowYourShips)
            bot_field.pr_all(screen, print_ships=ShowEnemyShips)

            # put clear button on the screen
            screen.blit(RestartImg, (0, 0))

            for i in player_field.field:
                for j in i:
                    if j.status == "part_ship":
                        player_ship_count += 1
            for i in bot_field.field:
                for j in i:
                    if j.status == "part_ship":
                        bot_ship_count += 1

            if player_ship_count == 0 and first_move:
                # the message "You lose!" appears here
                screen.blit(YouLoseImg, (0, 0))

                if IsSounds and can_go:
                    PlaySound("Lose")

                can_go = False

            if bot_ship_count == 0 and first_move:
                # the message "You win!" appears here
                screen.blit(YouWinImg, (0, 0))

                if IsSounds and can_go:
                    PlaySound("Win")
                
                can_go = False

            if can_go and not do_ship:
                screen.blit(GameStart, (0, 0))
            
            if can_go and do_ship:
                screen.blit(RandomShipGenImg, (0, 0))

            player_ship_count = 0    
            bot_ship_count = 0

            if bot_move:
                pg.display.flip()
                sleep(DelayBetweenMoves)
                # the bot chooses the place where it goes
                bot_move, coords, result_of_fire = bot_ob.cell_selection(player_comp_field) # y x
                y, x = coords

                # the bot makes a move on the place that he has chosen in advance
                player_field.synchronize(x, y)
                player_field.synchronize(x, y, player_comp_field)
                            
                if IsSounds:
                    if bot_move:
                        if result_of_fire == "Death":
                            PlaySound("EnemyDeath")
                                    
                        elif result_of_fire == "Hit":
                            PlaySound("EnemyHit")
                                        
                    else:
                        PlaySound("Skip")

                # print bot field for comp
                if PrintUserCompField:
                    print("User Field")
                    print_field(player_comp_field)
                    print("-----------------------------------------")
                                    
                player_ship_count = 0
                for i in player_field.field:
                    for j in i:
                        if j.status == "part_ship":
                            player_ship_count += 1

                if InfinityEnemyMoves:
                    if player_ship_count == 0:
                        bot_move = False
                        break   
                    bot_move = True
            else:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        is_game = False
                        return_num_ships()
                        break
                    
                    elif (event.type == pg.MOUSEBUTTONDOWN) and (pg.mouse.get_pressed(num_buttons=3)[0]):
                        x, y = pg.mouse.get_pos()

                        # restart the game
                        if (158 <= x <= 866) and (55 <= y <= 167):
                            player_field = Field(108, 474)
                            bot_field = Field(596, 474)
                            bot_comp_field = create_field()
                            bot_field.do_ships(None, 0, True, bot_comp_field)
                            bot_field.normal_ships_image()
                            return_num_ships()
                            num_of_ships = 0
                            do_ship = True
                            player_comp_field = create_field()
                            first_move = False
                            can_go = True

                        # player arranges ships
                        if do_ship:
                            if (92 <= x <= 932) and (222 <= y <= 369) or RandomShipGen:
                                return_num_ships()
                                player_field = Field(108, 474)
                                player_comp_field = create_field()
                                player_field.do_ships(None, 0, True, player_comp_field)
                                player_field.normal_ships_image()
                                do_ship = False

                                if IsSounds:
                                    PlaySound("GameStart")

                            else:
                                changed, x, y = change_coords(x, y, 108, 474)
                                if changed:
                                    num_of_ships, ships_segments = player_field.do_ships((y, x), num_of_ships, False, player_comp_field)
                                    player_field.normal_ships_image()

                                if num_of_ships == 10 and ships_segments == 20:
                                    # the player completes the placement of ships
                                    return_num_ships()
                                    do_ship = False

                                    if IsSounds:
                                        PlaySound("GameStart")

                        elif can_go:
                            changed, x, y = change_coords(x, y, 598, 476)
                            if changed and bot_move == False: 
                                if bot_field.field[y][x].status in ("free_place", "part_ship"):
                                    s = Ship()

                                    # the player makes a move
                                    players_attack_result = s.fire(bot_comp_field, (y, x))
                                    bot_field.synchronize(x, y)
                                    bot_field.synchronize(x, y, bot_comp_field)
                                    first_move = True

                                    if IsSounds:
                                        if players_attack_result[0]:
                                            if players_attack_result[1] == "Hit":
                                                PlaySound("YouHit")
                                            elif players_attack_result[1] == "Death":
                                                PlaySound("YouDeath")

                                        else:
                                            PlaySound("Skip")

                                    if players_attack_result[0] == False:
                                        bot_move = True

                                    if PrintCompCompField:
                                        print("Comp Field")
                                        print_field(bot_comp_field)
                                        print("--------------------------")

                                    if InfinityYourMoves:
                                        players_attack_result = (True,)
                                else:
                                    players_attack_result = (True,)
                                

            pg.display.flip()

    if IsMusic:
        def Music():
            pg.init()
            PlayMusic("Base")
        
        Thread(target=game).start()
        Thread(target=Music).start()

    else:
        game()
