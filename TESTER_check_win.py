from Key_Class import Key_Class
from Listed_Player_Class import Listed_Player_Class
import numpy as np

# instantiate keys
Keys = Key_Class()

# instantiate player
Player = Listed_Player_Class(0)

Player.get_key("1man")
Player.get_key("2man")
Player.get_key("3man")

Player.get_key("3man")
Player.get_key("4man")
Player.get_key("5man")

Player.get_key("2man")
Player.get_key("3man")
Player.get_key("4man")

Player.get_key("2sok")
Player.get_key("3sok")
Player.get_key("4sok")

Player.get_key("1sok")
Player.get_key("1sok")

print(Player.check_win())

Player.__set_empty_hand__()
Player.get_key("1tong")
Player.get_key("1tong")
Player.get_key("1tong")

Player.get_key("1tong")
Player.get_key("2tong")
Player.get_key("3tong")

Player.get_key("2man")
Player.get_key("3man")
Player.get_key("4man")

Player.get_key("2sok")
Player.get_key("3sok")
Player.get_key("4sok")

Player.get_key("2tong")
Player.get_key("2tong")

print(Player.check_win())