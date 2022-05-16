from argparse import ArgumentParser
import random
import sys



"""A turn based fantasy game that allows users to pick their character and power to fight against main monster"""

class Game:
    """Steps for playing the game
    
    Attributes:
        names (list): 
    """
    def __init__(self):
        """Initializes Game object.
        
        Side effects:
            Sets the names attributes
        """
        self.names = ['Pikachu','Scizor','Snorlax','Ninetales','Squirtle','Charizard']
        self.health = 100
        self.hp_val = 20
              
    def Attack(self):
        """Specifies method of attack.
        """
        
        attack_method = int(input('choose attack method (attack - 1, special attack - 2)'))
        hp_subtract_special= random.randint(2,6)
        hp_subtract_normal = random.randint(1,3)
        special_attack_damage = random.randint(8,30)
        normal_attack_damage = random.randint(2,15)
        if attack_method == 1:
            self.hp_val-= hp_subtract_normal
            self.health -= normal_attack_damage
        elif attack_method == 2:
            self.hp_val -= hp_subtract_special
            self.health -= special_attack_damage
        
    def Turn(self,opponent):
            """Allows player to take turns
            """
            player1 = input('Choose your character!(Pikachu,Scizor,Snorlax,Ninetales,Squirtle,Charizard)')
            opponent = random.choice(self.names)
            count = 0
            
         
        
    def Surrender():
        """Allows player to surrender
        """
    def Health():
        """Displays a health/XP bar that changes based on attacks
        """
    def NextBattle():
        """Allows users to continue playing and move up to the next battle
        """


class Monster:
    """Class for the monster the user will fight against.
    
    Attributes:
        name (str): 
        power (str): 
    """
    def __init__(self, name, power):
        """Initializes Monster object
        
        Side effects:
            Sets the name and power attributes
        """
    def Player_monster():
        """ Displays player's monsters
        """
    def Computer_monster():
        """Displays computer monsters
        """
    def Player_Skill_list():
        """Displays Players skill list
        """
    def Monster_skill_list():
        """Displays monsters skill list
        """


if __name__ == "__main__": 
    args = parse_args(sys.argv[1:])
    main(args.file)
