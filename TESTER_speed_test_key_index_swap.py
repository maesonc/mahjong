from Key_Class import Key_Class
from Listed_Player_Class import Listed_Player_Class
import time

Player = Listed_Player_Class(1)

start = time.time()

for _ in range(1000):
    Keys = Key_Class()
    for _ in range(144):
        intermediate_key = Keys.give_key()
        intermediate_key_token = Player.key_name_to_index(intermediate_key)
        if intermediate_key_token != (-1, -1):
            Player.key_index_to_name(intermediate_key_token[0], intermediate_key_token[1])

print('{0:.16f}'.format(time.time() - start))