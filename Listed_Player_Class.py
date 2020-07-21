from Key_Class import Key_Class
import numpy as np

class Listed_Player_Class:

    key_dictionary = Key_Class.key_dictionary

    def __init__(self, player_position):

        self.player_number = player_position
        
        if 0 <= self.player_number and self.player_number <= 3:
            pass
        else:
            raise AssertionError("Cannot instantiate player with number not between 0 and 3!")

        self.__set_empty_hand__()

        self.__error_string__ = "Player " + str(self.player_number) + " error! "


    # clears the players hand
    def __set_empty_hand__(self):
        # store suited keys as arrays instead to make it easier to check_win
        # dim0 = suit; 0 = man, 1 = sok, 2 = tong, 3 = no_suit
        # dim1 = rank; index starting from 1, so element 0 is unused
        self.keys_in_hand = np.zeros((4, 10))
        self.flowers_in_hand = np.zeros(5)

        # our list of seen THROWN keys, this does not include the keys in our hand
        # only the list of all keys thrown in the thrown pile
        self.keys_seen = np.zeros((4, 10))
        self.flowers_seen = np.zeros(5)

        # pong and chi in hands
        self.__pong_in_hand__ = np.zeros((4, 10))
        self.__chi_in_hand__ = np.zeros((4, 10))
        self.__pong_done__ = 0
        self.__chi_done__ = 0

        self.__allowable_keys_in_hand__ = 13


    # checks if the key is in the dictionary
    def check_if_key_in_dictionary(self, key):
        if key not in self.key_dictionary:
            raise Exception(self.__error_string__ + "Unknown key!")


    # checks if the key is part of suits
    def __check_if_key_is_suits__(self, key):
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

        if not self.__check_if_key_is_suits__(key):
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
            raise Exception(self.__error_string__ + "Attempted to convert unknown key!")

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
                raise Exception(self.__error_string__ + "Attempted to convert unknown key!")


    # count number of keys owned
    def count_keys(self):
        return np.sum(self.keys_in_hand) + np.sum(self.__pong_in_hand__) + np.sum(self.__chi_in_hand__)


    # count number of keys including flowers
    def count_keys_with_flowers(self):
        return self.count_keys() + np.sum(self.flowers_in_hand)


    # get all for keys, pong, and chis
    def __string_all__(self, key_set):
        if np.shape(key_set) != np.shape(self.keys_in_hand):
            raise AssertionError(self.__error_string__ + "Unknown key set, can't convert to stringarray")

        key_strings = []
        for suit_index, keys in enumerate(key_set):
            for rank_index, key in enumerate(keys):
                for _ in range(int(key)):
                    key_strings.append(self.key_index_to_name(suit_index, rank_index))
        return key_strings


    # return all keys as an array of key names, including pong and chi
    def string_all_keys(self):
        return self.__string_all__(self.keys_in_hand + self.__pong_in_hand__ + self.__chi_in_hand__)

    
    # returns all pongs as an array of key names
    def string_all_pong(self):
        return self.__string_all__(self.__pong_in_hand__)


    # returns all chis as an array of key names
    def string_all_chi(self):
        return self.__string_all__(self.__chi_in_hand__)

    
    # returns all free keys as an array of key names, without pong and chi
    def string_all_free_keys(self):
        return self.__string_all__(self.keys_in_hand)


    # return flowers as array of flower names
    def string_all_flowers(self):
        key_strings = []
        for flower_number, count in enumerate(self.flowers_in_hand):
            for _ in range(int(count)):
                key_strings.append('fa' + str(flower_number))
        return key_strings


    # adds a key and sorts it into our own hand
    # returns an indicator, if true then we have received a flower and it is our turn again
    def add_key(self, key):

        # sanity check for number of keys in hand
        if self.count_keys() > self.__allowable_keys_in_hand__:
            raise AssertionError(self.__error_string__ + "Attempted to receive key when there are already more than " + str(self.__allowable_keys_in_hand__ + 1) + " keys in hand!")

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
            raise AssertionError(self.__error_string__ + "Attempted to throw away a key we do not own!")

        return key


    # add key to our seen list
    def seen_key(self, key):
        suit, rank = self.key_name_to_index(key)
        if suit != -1:
            self.keys_seen[suit][rank] += 1
        else:
            flower_rank = int(key[-1])
            self.flowers_seen[flower_rank] += 1


    # helper function for check pong/kong to prevent repetition of code
    def __check_double_triplet__(self, key, count):
        suit_index, rank_index = self.key_name_to_index(key)
        
        if self.keys_in_hand[suit_index][rank_index] == count:
            return True

        return False

    
    # helper function for do pong/kong to prevent repetition of code
    def __do_double_triplet__(self, key, count):
        suit_index, rank_index = self.key_name_to_index(key)
        
        self.keys_in_hand[suit_index][rank_index] -= count
        self.__pong_in_hand__[suit_index][rank_index] += count
        self.__pong_done__ += 1

        if self.keys_in_hand[suit_index][rank_index] != 0:
            raise AssertionError(self.__error_string__ + "Something went wrong, we still have " + key + " in hand even after pong x" + str(count) + "!")


    # checks if pong is available
    def check_pong(self, key):
        return self.__check_double_triplet__(key, 2)


    # performs pong, shifts pong keys to __pong_in_hand__ list and
    # removed from keys_in_hand
    def do_pong(self, key):
        self.__do_double_triplet__(key, 2)


    # checks if kong is available
    def check_kong(self, key):
        return self.__check_double_triplet__(key, 3)


    # performs kong, shifts kong keys to __pong_in_hand__ list and
    # removed from keys_in_hand
    def do_kong(self, key):
        self.__do_double_triplet__(key, 3)

    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE
    # MAESON PUT YOUR CHI HERE


    # preliminary check_win for non-suited
    def __prelim_check_win__(self, keys_left):
        # if our non-suited keys only have one of their kind
        # we have neither eyes, kong, or pong, no solution
        for key in keys_left[-1]:
            if key == 1:
                return False

        return True


    # Checks if our hand is a winning hand
    def __recursive_check_win__(self, keys_left):
        #print(keys_left)

        # check for eyes
        if np.sum(keys_left) == 2:
            for keys in keys_left:
                for key in keys:
                    if key == 2:
                        return True

        # recursively find sets in our hand, one at a time
        for suit_index, keys in enumerate(keys_left):
            for rank_index, key in enumerate(keys):
                # only proceed if the key we're looking at exists
                if key > 0:
                    # solve for suited keys first
                    if 0 <= suit_index and suit_index <= 2:
                        # upwards look for sequential
                        if rank_index <= 7:
                            # check if we have a sequential set
                            if (keys_left[suit_index][rank_index+0] > 0
                            and keys_left[suit_index][rank_index+1] > 0
                            and keys_left[suit_index][rank_index+2] > 0):
                                # if we have a sequential set, remove that set from keys_left
                                keys_left[suit_index][rank_index+0] -= 1
                                keys_left[suit_index][rank_index+1] -= 1
                                keys_left[suit_index][rank_index+2] -= 1

                                # pass remaining keys to recursively check
                                # print("One sequential found")
                                if self.__recursive_check_win__(keys_left):
                                    return True
                                else:
                                    # if the sequential that we found is not a winning path
                                    # we add the sequential back to the set and move one key to the right
                                    # and recheck
                                    keys_left[suit_index][rank_index+0] += 1
                                    keys_left[suit_index][rank_index+1] += 1
                                    keys_left[suit_index][rank_index+2] += 1

                    # if we don't have a sequential set
                    # or if our key index is more than 7 (because sequential lookup is 7, 8 ,9)
                    # or if we're looking at non-suits
                    if key == 3:
                        # we have 3 of a kind, remove from keys_left
                        # pass remaining keys to recursively check
                        keys_left[suit_index][rank_index] -= 3
                        # print("One set found")
                        if self.__recursive_check_win__(keys_left):
                            return True
                        else:
                            # if the set we found is not a winning path
                            # add the set back to the set and move one step to the right
                            # and recheck
                            keys_left[suit_index][rank_index] += 3

        return False


    # check_win function that ties in prelim and recursive
    def check_win(self):
        if self.__prelim_check_win__(self.keys_in_hand):
            if self.__recursive_check_win__(self.keys_in_hand):
                return True

        return False

                                



