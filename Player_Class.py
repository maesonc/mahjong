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

    def throw_key(self, key):

        if key not in self.key_dictionary:
            raise Exception("Player " + str(self.player_number) + " error! Attempted to throw away non-esistent key!")

        if key not in self.keys_in_hand:
            raise Exception("Player " + str(self.player_number) + " error! Attempted to throw away key that's not in hand!")
        elif self.keys_in_hand[key] > 1:
            self.keys_in_hand[key] -= 1
        else:
            del self.keys_in_hand[key]

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
