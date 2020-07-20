from Key_Class import Key_Class
from Player_Class import Player_Class
import numpy as np


# instantiate keys
Keys = Key_Class()

# instantiate players
Player = []
for i in range(4):
    Player.append(Player_Class(i))

intermediate_key = Keys.give_key()
Player[0].get_key(intermediate_key)
for _ in range(13):
    for i in range(4):
        intermediate_key = Keys.give_key()
        Player[i].get_key(intermediate_key)

key_count = [0, 0, 0, 0]
for i in range(4):
    # print(Player[i].keys_in_hand)
    
    for count in Player[i].keys_in_hand.values():
        key_count[i] += count

    print("Player " + str(i) + " has " + str(key_count[i]) + " in hand.")

remaining_key_count = 0
for count in Keys.available_keys.values():
    remaining_key_count += count

print("Stack" + " has " + str(remaining_key_count) + " in hand.")

total_key_count = np.sum(key_count) + remaining_key_count
print("Total key count is " + str(total_key_count))