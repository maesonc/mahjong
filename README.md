# Deep Mahjong
Mahjong project to build a game engine for mahjong, and hopefully build an RL agent to play the game.

## Prerequisites
Non for now.

## Class Descriptions

### Key_Class
Class that provides a centralized location for all the keys, handles all outputs of available keys from the centre stack.

- **give_key()**
    - Gives a string representing the given key.
    - Returns: key_name (string)

### Player_Class
Individual template for creating players (default 4), handles keys in hand for individual players, abilities to pong/chi

- **get_key(key_name)**
    - Adds key_name to self, ideally pulled from main script from Key_Class

- **check_pong()**
    - Checks whether pong is available with keys in self

- **do_pong(pong_available)**
    - Performs pong based on whether pong_available is true, pong_available to be pulled form main (to check if previous player has pong-ed)

- **check_chi(previous_player_number)**
    - Checks whether chi is available with keys in self, previous_player_number to be received from main (to check if precedence is followed)

- **do_chi(chi_available)**
    - Performs chi based on whether chi_available is true, chi_available to be pulled form main (to check if previous player has chi-ed)

- **is_win(is_win)**
    - Declares internal win based on is_win received from Reward_Class

- **count_points(points)**
    - Sets internal points based on points received from Reward_Class

### Reward_Class
Static Class to take in player keys and output is_win and points