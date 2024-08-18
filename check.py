from classes import *
from functions import *
from time import sleep

return_num_ships()

field = create_field()

Ship.create_ship(field, (5, 5))
Ship.create_ship(field, (6, 5))
Ship.create_ship(field, (7, 5))
print_field(field)
print("--------------------")
sleep(5)

bot = Bot()


for i in range(20):
    bot.fire(field)
    print_field(field)
    print("--------------------------------")
    sleep(1)



