# Deep Mahjong
Mahjong project to build a ame engine for mahjong, and hopefully build an RL agent to play the game.

## Prerequisites
Non for now.

## Class Descriptions

### Key_Class
Class that provides a centralized location for all the keys, handles all outputs of available keys from the centre stack.

- **give_key()**
    - Gives a string representing the given key.
    - Returns: key_name (string)

### Player_Class
Individual template for creating players (default 4), handles keys in hand for individual players, abilities to pong/chi, calls `calc_points` and check_win from `point_system` class

- **get_key(key_name)**
    - Adds key_name to self, ideally pulled from main script 