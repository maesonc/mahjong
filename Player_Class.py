from Key_Class import Key_Class

class Player_Class:

    player_number = None
    key_dictionary = Key_Class.key_dictionary
    keys_in_hand = {}

    pong_in_hand = {}
    chi_in_hand = {}
    pong_done = 0
    chi_done = 0

    allowable_keys_in_hand = 13

    error_string = None



    def __init__(self, player_position):
        self.player_number = player_position

        if 1 <= self.player_number and self.player_number <= 4:
            pass
        else:
            raise AssertionError("Cannot instantiate player with with number not between 1 and 4!")

        self.error_string = "Player " + str(self.player_number) + " error! "




    def check_if_key_in_dictionary(self, key):
        if key not in self.key_dictionary:
            raise Exception("Player " + str(self.player_number) + " error! Unknown key!")




    def get_key(self, key_name):
        self.check_if_key_in_dictionary(key_name)

        number_of_keys_in_hand = 0

        for key_count in self.keys_in_hand.values():
            number_of_keys_in_hand += key_count

        if number_of_keys_in_hand > self.allowable_keys_in_hand:
            raise AssertionError(self.error_string + "Attempted to receive key when there are already more than 13 keys in hand!")

        if key_name not in self.keys_in_hand:
            self.keys_in_hand[key_name] = 1
        else:
            self.keys_in_hand[key_name] += 1




    def throw_key(self, key):
        self.check_if_key_in_dictionary(key)

        if key not in self.keys_in_hand:
            raise Exception(self.error_string + "Attempted to throw away key that's not in hand!")
        elif self.keys_in_hand[key] > 1:
            self.keys_in_hand[key] -= 1
        else:
            del self.keys_in_hand[key]



    
    def check_pong(self, option_key):
        self.check_if_key_in_dictionary(option_key)

        if option_key in self.keys_in_hand:
            if self.keys_in_hand[option_key] == 2:
                return True

        return False




    def do_pong(self, option_key):
        self.check_if_key_in_dictionary(option_key)

        if option_key in self.keys_in_hand:
            self.keys_in_hand[option_key] += 1
        else:
            raise AssertionError(self.error_string + "Tried to pong a key that we do not own")

        if self.keys_in_hand[option_key] == 3:
            self.pong_in_hand[option_key] = 3
            self.pong_done += 1
            return
        else:
            raise AssertionError(self.error_string + "We do not have exactly 3 of the same key for display after pong!")




    def check_kong(self, option_key):
        self.check_if_key_in_dictionary(option_key)

        if option_key in self.keys_in_hand:
            if self.keys_in_hand[option_key] == 3:
                return True

        return False




    def do_kong(self, option_key):
        # we treat kong the same as a pong for now
        self.check_if_key_in_dictionary(option_key)

        if option_key in self.keys_in_hand:
            self.keys_in_hand += 1
        else:
            raise AssertionError(self.error_string + "Triede to kng a key that we do not own")

        if self.keys_in_hand[option_key] == 4:
            self.pong_in_hand[option_key] = 4
            self.pong_done += 1
            self.allowable_keys_in_hand += 1
            return
        else:
            raise AssertionError(self.error_string + "We do not have exactly 4 of the same key for display after kong!")

        return True
        


    def check_chi(self, previous_player_number, option_key):
        pass

    def do_chi(self, option_key):
        pass

    
    
    
    def count_points(self):
        pass




    def is_win(self):
        complete_sets = 0

        complete_sets += self.pong_done + self.chi_done

        current_hand_for_check = self.keys_in_hand

        for key, value in self.chi_in_hand:
            current_hand_for_check[key] -= value
            
            if current_hand_for_check[key] == 0:
                del current_hand_for_check[key]
            elif current_hand_for_check[key] < 0:
                raise Exception(self.error_string + "Chi set has more keys than in keys in hand during check win!")

        for key, value in self.pong_in_hand:
            current_hand_for_check[key] -= value

            if current_hand_for_check[key] == 0:
                del current_hand_for_check[key]
            elif current_hand_for_check[key] < 0:
                raise Exception(self.error_string + "Pong set has more keys than in keys in hand during check win!")

        for key, value in current_hand_for_check:
            if value >= 3:
                complete_sets += 1
                current_hand_for_check[key] -= 3

                if current_hand_for_check[key] == 0:
                    del current_hand_for_check[key]

        # INSERT CHECK IF SEQUENTIAL CODE HERE

        if complete_sets == 4:
            if len(current_hand_for_check) == 1:
                if list(current_hand_for_check.values())[0] == 2:
                    return True

        return False
                
            


