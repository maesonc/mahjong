# Deep Mahjong
Mahjong project to build a game engine for mahjong, and hopefully build an RL agent to play the game.

## Prerequisites
### Code Standards
- 2 blank lines before start of new function in class
- be as descriptive as possible (ie: number_of_keys, ~~num_keys~~)

- **FUNCTION_NAME**
    - DESCRIPTION
    - Returns:

## Class Descriptions

### Key_Class
Class that provides a centralized location for all the keys, handles all outputs of available keys from the centre stack. Also manages keys in throwaway pile

- **give_key()**
    - Gives a string representing the given key
    - Returns: key_name (string)

- **throwaway_key(throw_key)**
    - Adds key to throwaway pile

- **give_latest_thrown_key()**
    - Gives string representing latest thrown key
    - Return: latest_thrown_key(string)

### Player_Class
Individual template for creating players (default 4), handles keys in hand for individual players, abilities to pong/chi

- **check_if_key_in_dictionary(key)** - Jet
    - Checks if key is in dictionary

- **get_key(key_name)** - Jet
    - Adds key_name to self, ideally pulled from main script from Key_Class

- **throw_key(key_name)** - Maeson
    - Throws a key from hand

- **check_pong(option_key)** - Jet
    - Checks whether pong is available with keys in self
    - Returns: pong_doable (bool)

- **do_pong(option_key)**
    - Performs pong

- **check_chi(previous_player_number, option_key)** - Maeson
    - Checks whether chi is available with keys in self, previous_player_number to be received from main (to check if precedence is followed)
    - Returns: chi_doable (bool)

- **do_chi(option_key)**
    - Performs chi

- **is_win()**
    - Checks the amount of points total with in-hand keys
    - Returns: points

- **count_points()**
    - Checks for hand completion with in-hand keys
    - Returns: (percent_complete, is_win)


### Listed_Player_Class
Same as Player_Class but stores keys in arrays instead

- **check_if_key_in_dictionary**
    - Checks if key is legit from dictionary, throws error otherwise

- **__check_if_key_is_suits__**
    - Checks if the key is from man, sok, tong
    - Returns: bool

- **key_name_to_index**
    - returns tuple of (suit_index, rank_index) of a given key name string, index refers to keys_in_hand
    - Returns: tuple (int, int)

- **key_index_to_name**
    - returns key name string given index of key
    - Returns: string

- **count_keys**
    - Counts number of keys owned, minus flowers
    - Returns: int

- **count_keys_with_flowers**
    - Counts number of keys owned, including flowers
    - Returns: int

- **get_all_keys**
    - Returns list of all keys owned as strings, excluding flowers
    - Returns: [string, ...]

- **get_all_flowers**
    - Returns list of all flowers owned as strings
    - Returns: [string, ...]

- **get_key**
    - adds key to ourself, returns True if we have received a flower to indicate we need to take another key
    - Returns: bool

- **throw_key**
    - throws away a key based on name string

- **seen_key**
    - adds key to our list of seen keys, ie: key in the centre exposed pile

- **check_pong**
    - checks if we can do pong
    - Returns: bool

- **do_pong**
    - performs pong

- **check_kong**
    - checks if we can do kong
    - Returns: bool

- **do_kong**
    - performs kong