from Key_Class import Key_Class
from Listed_Player_Class import Listed_Player_Class
import numpy as np

# instantiate keys
Keys = Key_Class()

# instantiate player
Player = Listed_Player_Class(0)

Player.add_key("1man")
Player.add_key("2man")
Player.add_key("3man")

Player.add_key("3man")
Player.add_key("4man")
Player.add_key("5man")

Player.add_key("2man")
Player.add_key("3man")
Player.add_key("4man")

Player.add_key("2sok")
Player.add_key("3sok")
Player.add_key("4sok")

Player.add_key("1sok")
Player.add_key("1sok")

print(Player.check_win())

Player.__set_empty_hand__()
Player.add_key("1tong")
Player.add_key("1tong")
Player.add_key("1tong")

Player.add_key("1tong")
Player.add_key("2tong")
Player.add_key("3tong")

Player.add_key("2man")
Player.add_key("3man")
Player.add_key("4man")

Player.add_key("2sok")
Player.add_key("3sok")
Player.add_key("4sok")

Player.add_key("2tong")
Player.add_key("2tong")

print(Player.check_win())