from classes import *
from functions import *
from time import sleep

field = create_field()

Ship.ship_gen(field, 0, True, 0)
print_field(field)
print("--------------------")
# sleep(5)

bot = Bot()


for i in range(50):
    bot.fire(field)
    print_field(field)
    print("--------------------------------")
#     # sleep(1)

return_num_ships()



