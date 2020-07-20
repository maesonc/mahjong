from Key_Class import Key_Class
from Player_Class import Player_Class

# instantiate keys
Keys = Key_Class()

# instantiate players
Player = []
for i in range(4):
    Player.append(Player_Class(i))

intermediate_key = Keys.give_key()
Player[0].get_key(intermediate_key)
for _ in range(15):
    for i in range(4):
        intermediate_key = Keys.give_key()
        Player[i].get_key(intermediate_key)
