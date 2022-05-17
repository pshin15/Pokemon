# Pokemon

INST326 Final Project

Our program is a turn based fantasy game. It starts with asking the players names. When it's the players turn,
it gives them 2 options; attack or surrender. Then asks the user to choose their skill to attack with; sword slash 
or sword dash. Once the player selects, the program displays both players and computer players' attacks and how much 
damage they caused. It also displays the new health status, showcasing how many health points they have left. This
will repeat until the health point reaches zero. The program will print out if you win or lose. It’ll give the player 
the option to move onto the next battle and continue playing. 

Game progression: 
Player is presented with two dungeons to enter. Once entering one of the dungeons he will face a wave of monsters that
get progressively stronger. 

Classes:
-Player
-Game
-Monsters

Player class Method:
-__init__()
-damage()
-select_skills()

Game class methods:
-__init()
-__str__()
-turn()
-monster_turn()
-display_hp()
-check_win()
-hp_rest()
-surrender()

Attributes: turns, names
-__init__()
-Turn()
-Attack()
-Surrender()
-Health()
-NextBattle()

Monster class methods:
-__init__()
-damage()
-select_skills()

Attributes: name, power
-__init__()
-Player_monster
-Computer_monster
-Player_Skill_list()
-Monster_skill_list()

Functions:
-conditional expressions
-optional parameters and/or use of keyword arguments
-f-strings
-the ArgumentParser class
-set operations on sets or frozensets
-super()
-magic methods other than __init__()
 
Sources:
https://www.evennia.com/docs/latest/Turn-based-Combat-System.html 
This source was used to see how a turn based combat system would look like. Wanted to see what combats and 
rules we should include in our code.

https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html 
This source was used to help with docstrings 








