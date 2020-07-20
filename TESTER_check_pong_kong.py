from Key_Class import Key_Class
from Listed_Player_Class import Listed_Player_Class
import numpy as np

# instantiate keys
Keys = Key_Class()

# instantiate player
Player = Listed_Player_Class(0)

for _ in range(2):
    Player.add_key('1man')

print("Current keys in hand: ")
print(Player.keys_in_hand)
print(" ")

if Player.check_pong('1man'):
    print("pong legit")
    Player.do_pong('1man')
    print(Player.keys_in_hand)
    print(Player.__pong_in_hand__)
    print(Player.__pong_done__)
else:
    print("pong not legit")

if Player.check_kong('1man'):
    print("kong legit")
    Player.do_kong('1man')
    print(Player.keys_in_hand)
    print(Player.__pong_in_hand__)
    print(Player.__pong_done__)
else:
    print("kong not legit")
