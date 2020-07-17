class Key_Class:

    available_keys = {}

    def __init__(self):
        self.available_keys['1man'] = 4
        self.available_keys['2man'] = 4
        self.available_keys['3man'] = 4
        self.available_keys['4man'] = 4
        self.available_keys['5man'] = 4
        self.available_keys['6man'] = 4
        self.available_keys['7man'] = 4
        self.available_keys['8man'] = 4
        self.available_keys['9man'] = 4

        self.available_keys['1sok'] = 4
        self.available_keys['2sok'] = 4
        self.available_keys['3sok'] = 4
        self.available_keys['4sok'] = 4
        self.available_keys['5sok'] = 4
        self.available_keys['6sok'] = 4
        self.available_keys['7sok'] = 4
        self.available_keys['8sok'] = 4
        self.available_keys['9sok'] = 4
        
        self.available_keys['1tong'] = 4
        self.available_keys['2tong'] = 4
        self.available_keys['3tong'] = 4
        self.available_keys['4tong'] = 4
        self.available_keys['5tong'] = 4
        self.available_keys['6tong'] = 4
        self.available_keys['7tong'] = 4
        self.available_keys['8tong'] = 4
        self.available_keys['9tong'] = 4

        self.available_keys['dong'] = 4
        self.available_keys['nan'] = 4
        self.available_keys['si'] = 4
        self.available_keys['bei'] = 4

        self.available_keys['hongzhong'] = 4
        self.available_keys['chengchoi'] = 4
        self.available_keys['bakban'] = 4

        self.available_keys['flower1'] = 2
        self.available_keys['flower2'] = 2
        self.available_keys['flower3'] = 2
        self.available_keys['flower4'] = 2

        number_of_keys = 0
        for count in self.available_keys.values():
            number_of_keys += count

        assert number_of_keys == 144, "Error! Initialized keys do not total to 144!"
        
    def give_key(self):
        pass

    def throwaway_key(self, throw_key):
        pass
