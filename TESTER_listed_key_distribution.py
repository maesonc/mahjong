from Key_Class import Key_Class
from Listed_Player_Class import Listed_Player_Class
import numpy as np

# instantiate keys
Keys = Key_Class()

# instantiate players
Player = []
for i in range(4):
    Player.append(Listed_Player_Class(i))

# start key distribution, first player gets one extra key at end of draw
intermediate_key = Keys.give_key()

for _ in range(13):
    for i in range(4):
        intermediate_key = Keys.give_key()
        Player[i].get_key(intermediate_key)

Player[0].get_key(intermediate_key)


# sanity check the number of keys each player has, number of keys left in pile, and total keys
key_counts = [0, 0, 0, 0, 0]

for i in range(4):
    key_counts[i] = Player[i].count_keys_with_flowers()
    print("Player " + str(i) + " has " + str(key_counts[i]) + " in hand.")
    
    # print the key list for each player including flowers
    keys_list = Player[i].get_all_keys()
    keys_list.extend(Player[i].get_all_flowers())
    print("Player" + str(i) + " keys list: ")
    print(keys_list)
    print(" ")


key_counts[4] = Keys.count_keys()
print("Stack" + " has " + str(key_counts[4]) + " remaining.")

total_key_count = np.sum(key_counts)
print("Total key count is " + str(total_key_count))