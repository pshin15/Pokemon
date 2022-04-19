"""A turn based fantasy game that allows users to pick their character and power to fight against main monster"""

class Game:
    """Steps for playing the game
    
    Attributes:
        turns (int):
        names (str): 
    """
    def __init__(self, turns, names):
        """Initializes Game object.
        """
    def Turn():
        """Allows player to take turns
        """
    def Attack():
        """Specifies method of attack.
        """
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
