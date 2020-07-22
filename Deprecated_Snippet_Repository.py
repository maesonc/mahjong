# returns a key name string given a key index
def key_index_to_name(self, suit_index, rank_index):
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