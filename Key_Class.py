import random

class Key_Class:

    NUMBER_OF_KEYS = 144

    available_keys = {}
    thrown_keys = {}
    key_dictionary= [
        '1man', '2man', '3man', '4man', '5man', '6man', '7man', '8man', '9man',
        
        '1sok', '2sok', '3sok', '4sok', '5sok', '6sok', '7sok', '8sok', '9sok',
        
        '1tong', '2tong', '3tong', '4tong', '5tong', '6tong', '7tong', '8tong', '9tong',
        
        'dong', 'nan', 'sai', 'bok',
        
        'hongzhong', 'chengchoi', 'bakban',
        
        'fa1', 'fa2', 'fa3', 'fa4'
        ]

    def __init__(self):
        for key_name in self.key_dictionary:
            self.available_keys[key_name] = 4

        self.available_keys['fa1'] = 2
        self.available_keys['fa2'] = 2
        self.available_keys['fa3'] = 2
        self.available_keys['fa4'] = 2

        number_of_keys = 0
        for count in self.available_keys.values():
            number_of_keys += count

        assert number_of_keys == self.NUMBER_OF_KEYS, "Error! Initialized keys do not total to 144!"
        
    def give_key(self):
        if len(self.available_keys) < 1:
            raise Exception("Error! Attempted to draw key from completed pile!")

        random_key = random.choice(list(self.available_keys))

        self.available_keys[random_key] -= 1
        if self.available_keys[random_key] == 0:
            del self.available_keys[random_key]

        return random_key

    def throwaway_key(self, throw_key):
        assert throw_key in self.key_dictionary, "Error! Attempted to throw away non-existent key!"

        if throw_key not in self.thrown_keys:
            self.thrown_keys[throw_key] = 1
        else:
            assert self.thrown_keys[throw_key] < 4, "Error! Attempted to throw away key that's been thrown four times!"
            self.thrown_keys[throw_key] += 1

        
