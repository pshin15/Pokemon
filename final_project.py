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
    def Surrender(player):
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
