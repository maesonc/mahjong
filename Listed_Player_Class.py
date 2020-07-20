from Key_Class import Key_Class
import numpy as np

class Listed_Player_Class:

    key_dictionary = Key_Class.key_dictionary

    def __init__(self, player_position):

        self.player_number = None

        # store suited keys as arrays instead to make it easier to check_win
        # dim0 = suit; 0 = man, 1 = sok, 2 = tong, 3 = no_suit
        # dim1 = rank; index starting from 1, so element 0 is unused
        self.keys_in_hand = np.zeros((4, 10))
        self.flowers_in_hand = np.zeros(5)

        # our list of seen THROWN keys, this does not include the keys in our hand
        # only the list of all keys thrown in the thrown pile
        self.keys_seen = np.zeros((4, 10))
        self.flowers_seen = np.zeros(5)

        # pong and chi in hands are just string names appended as a list
        # we don't care to index these since they are fixed once performed
        # we only store them to help maintain fixed number of keys in hand
        self.pong_in_hand = []
        self.chi_in_hand = []
        self.pong_done = 0
        self.chi_done = 0

        self.allowable_keys_in_hand = 13

        self.error_string = "Player " + str(self.player_number) + " error! "

        self.player_number = player_position

        if 0 <= self.player_number and self.player_number <= 3:
            pass
        else:
            raise AssertionError("Cannot instantiate player with number not between 0 and 3!")


    # checks if the key is in the dictionary
    def check_if_key_in_dictionary(self, key):
        if key not in self.key_dictionary:
            raise Exception(self.error_string + "Unknown key!")


    # checks if the key is part of suits
    def check_if_key_is_suits(self, key):
        if key[0].isnumeric():
            return True
        else:
            return False


    # returns tuple of (key_suit, key_rank) given a key
    # otherwise, returns (-1, -1) for flowers
    def key_name_to_index(self, key):
        self.check_if_key_in_dictionary(key)

        key_suit = -1
        key_rank = -1

        if not self.check_if_key_is_suits(key):
            if key == 'dong':
                key_suit = 3
                key_rank = 1
            elif key == 'nan':
                key_suit = 3
                key_rank = 2
            elif key == 'sai':
                key_suit = 3
                key_rank = 3
            elif key == 'bok':
                key_suit = 3
                key_rank = 3
            elif key == 'hongzhong':
                key_suit = 3
                key_rank = 5
            elif key == 'chengchoi':
                key_suit = 3
                key_rank = 6
            elif key == 'bakban':
                key_suit = 3
                key_rank = 7

            # if the key is a flower key, it will auto return (-1, -1)

        else:
            # this loop will only begin when the key is a suited key
            key_rank = int(key[0])

            key_suit_name = key[1:]
            if key_suit_name == 'man':
                key_suit = 0
            elif key_suit_name == 'sok':
                key_suit = 1
            elif key_suit_name == 'tong':
                key_suit = 2

        return (key_suit, key_rank)

    

    # returns a key name string given a key index
    def key_index_to_name(self, suit_index, rank_index):
        if 0 <= suit_index and suit_index <= 3:
            if 1 <= rank_index and rank_index <= 9:
                pass
        else:
            raise Exception(self.error_string + "Attempted to convert unknown key!")

        # this line won't be reached if rank is not between 1-9 and
        # suit index is not between 0 and 3
        if 0 <= suit_index and suit_index <= 2:
            string_suit = None
            string_rank = str(rank_index)

            if suit_index == 0:
                string_suit = 'man'
            elif suit_index == 1:
                string_suit = 'sok'
            elif suit_index == 2:
                string_suit = 'tong'

            return string_rank + string_suit
        else:
            # we will only reach here if and only if suit_index = 3
            if rank_index == 1:
                return 'dong'
            elif rank_index == 2:
                return 'nan'
            elif rank_index == 3:
                return 'sai'
            elif rank_index == 4:
                return 'bok'
            elif rank_index == 5:
                return 'hongzhong'
            elif rank_index == 6:
                return 'chengchoi'
            elif rank_index == 7:
                return 'bakban'
            else:
                raise Exception(self.error_string + "Attempted to convert unknown key!")


    # count number of keys owned
    def count_keys(self):
        return np.sum(self.keys_in_hand) + len(self.pong_in_hand) + len(self.chi_in_hand)


    # count number of keys including flowers
    def count_keys_with_flowers(self):
        return self.count_keys() + np.sum(self.flowers_in_hand)


    # return all keys as an array of key names
    def get_all_keys(self):
        key_strings = []
        for suit_index, lists in enumerate(self.keys_in_hand):
            for rank_index, keys in enumerate(lists):
                for _ in range(int(keys)):
                    key_strings.append(self.key_index_to_name(suit_index, rank_index))
        return key_strings


    # return flowers as array of flower names
    def get_all_flowers(self):
        key_strings = []
        for flower_number, count in enumerate(self.flowers_in_hand):
            for _ in range(int(count)):
                key_strings.append('fa' + str(flower_number))
        return key_strings


    # gets a key and sorts it into our own hand
    # returns an indicator, if true then we have received a flower and it is our turn again
    def get_key(self, key):

        # sanity check for number of keys in hand
        if self.count_keys() > self.allowable_keys_in_hand:
            raise AssertionError(self.error_string + "Attempted to receive key when there are already more than " + str(self.allowable_keys_in_hand + 1) + " keys in hand!")

        # sort keys, automatically checks if key is legit
        suit, rank = self.key_name_to_index(key)

        if suit == -1:
            index = int(key[-1])
            self.flowers_in_hand[index] += 1
            return True
        else:
            self.keys_in_hand[suit][rank] += 1
            return False


    # throws away a key
    def throw_key(self, key):
        suit, rank = self.key_name_to_index(key)
        if self.keys_in_hand[suit][rank] > 0:
            self.keys_in_hand[suit][rank] -= 1
        else:
            raise AssertionError(self.error_string + "Attempted to throw away a key we do not own!")

        return key


    # add key to our seen list
    def seen_key(self, key):
        suit, rank = self.key_name_to_index(key)
        if suit != -1:
            self.keys_seen[suit][rank] += 1
        else:
            flower_rank = int(key[-1])
            self.flowers_seen[flower_rank] += 1


