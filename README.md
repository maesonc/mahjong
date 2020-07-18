# Deep Mahjong
Mahjong project to build a game engine for mahjong, and hopefully build an RL agent to play the game.

## Prerequisites
### Code Standards
- 4 blank lines before start of new function in class
- be as descriptive as possible (ie: number_of_keys, ~~num_keys~~)

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

- **get_key(key_name)**
    - Adds key_name to self, ideally pulled from main script from Key_Class

- **throw_key()** - Maeson
    - Throws a key from hand

- **check_pong(option_key)**
    - Checks whether pong is available with keys in self
    - Returns: pong_doable (bool)

- **do_pong(option_key)**
    - Performs pong

- **check_chi(previous_player_number, option_key)**
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
    
