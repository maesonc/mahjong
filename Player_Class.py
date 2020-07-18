from Key_Class import Key_Class

class Player_Class:

    player_number = None
    key_dictionary = Key_Class.key_dictionary
    keys_in_hand = {}

    def __init__(self, player_position):
        self.player_number = player_position
        
    def get_key(self, key_name):
        if key_name not in self.keys_in_hand.keys():
            self.keys_in_hand[key_name] = 1
        else:
            self.keys_in_hand[key_name] += 1

    def throw_key(self):
        pass

    def check_pong(self, option_key):
        pass

    def do_pong(self, option_key):
        pass

    def check_chi(self, previous_player_number, option_key):
        pass

    def do_chi(self, option_key):
        pass

    def count_points(self):
        pass

    def is_win(self):
        pass
