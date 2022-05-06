"""A turn based fantasy game that allows users to pick their character and power to fight against main monster"""

class Game:
    """Steps for playing the game
    
    Attributes:
        turns (int): The turns of the battles
        names (str): The name of the player
    """
    def __init__(self, turns, names):
        """Initializes Game object.
        """
    def Turn():
        """Allows player to take turns
        """
    def Attack(player,opponent,skill):
        """Specifies method of attack.

        Args:
            player (str): The player name
            opponent (str): Opponent Name
            skill (str): The name of the skill direct at the opponent
        """
    def Surrender(self, player): 
        """Allows player to surrender
        """
        if self.hp_val == 0:
            print(f"{self.names}, do you wish to continue?")
            options = ["Yes", "No"]
            x = random.choice(options)
            for option in options:
                if x == "Yes":
                    continue
                else:
                    break
    def Health():
        """Displays a health/XP bar that changes based on attacks
        """
        print(self.health)


class Monster:
    """Class for the monster the user will fight against.
    
    Attributes:
        name (str): name of the monster
        power (str): specific power of the monster
    """
    def __init__(self, name, power):
        """Initializes Monster object
        """
        self.name = name
        self.power = power
        
    def Player_monster(self):
        """ Displays player's monsters
        """
        choice = random.randint(1,2)
        self.player = choice - 1
        
    
    def Computer_monster(player):
        """Displays computer monsters
        """
        choice = random.randint(1,2)
        self.computer = choice - 1
        
       
    def Player_Skill_list(self):
        """Displays Players skill list
        """
        player_skill_list = []
        
        return player_skill
    
    def Monster_skill_list(player):
        """Displays monsters skill list
        """
        monster_skill_list = []
        
        return monster_skill

if __name__ == "__main__": 
    args = parse_args(sys.argv[1:])
    main(args.file)
