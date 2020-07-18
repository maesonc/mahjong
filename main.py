from Key_Class import Key_Class
from Player_Class import Player_Class

# instantiate keys
Keys = Key_Class()
Player1 = Player_Class(1)
Player1.get_key('1man')
Player1.get_key('2man')
print (Player1.keys_in_hand)
print (Player1.check_chi('4man'))

