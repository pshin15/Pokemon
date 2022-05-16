import random
from argparse import ArgumentParser

class player:
    """Creates a Player Class
    
    Attributes:
        name (str): Name of the Player
        s1 (str): Skill 1 of the Player
        s2 (str): Skill 2 of the Player
    """
    def __init__(self,name,s1,s2):
        """Sets up the attributes of the player object

        Args:
            name (str): Name of the Player
            s1 (str): Skill 1 of the Player
            s2 (str): Skill 2 of the Player
            
        Side effects:
            Initializes name and skills attributes.
        """
        self.name=name
        self.health=100
        self.skill=None
        self.s1=s1
        self.s2=s2
        self.skill_list=[self.s1,self.s2]
        
    def damage(self):
        """This is a randomized damage number that is increased if its a skill 2

        Returns:
            int : The amount of damage 
        """
        points=random.randint(25,35)
        if self.skill is self.skill_list[1]:
            points*1.2
        return points
    
    def select_skill(self):
        """Ask the user to select which skill to attack with
        """
        choice=int(input(f"Choose your skill to attack with:\n"
                         f"1({self.skill_list[0]}) or 2({self.skill_list[1]})\n"))
        self.skill = self.skill_list[(choice-1)]
        
        
class monster(player):
    """Subclass of Player class but its damage method and skills are randomly 
    chosen

    Args:
        player (Object): Player object
    """
    def __init__(self,name,s1,s2):
        """Sets the attributes of the player

        Args:
            name (str): The name of the AI monster
            s1 (str): Skill 1 of monster
            s2 (str): Skill 2 of monster
        
        Side effects:
            Initializes name and skills attributes.
        """
        super().__init__(name,s1,s2)
        
    
    def damage(self):
        """Calculates the damage numbers

        Returns:
            int: The damage number
        """
        points=random.randint(10,25)
        if self.skill is self.skill_list[1]:
            points*1.2
        return points
    
    def select_skill(self):
        """Randomly selects one of the skills to attack
        """
        self.skill= random.choice(self.skill_list)
        
class game:
    """Starts the game and battle between the Monster class and Player class
    """
    def __init__(self,p1,p2):
        """Sets the attibutes of game object

        Args:
            p1 (Object): Player 1 object
            p2 (Object): Player 2 object
        """
        self.p1=p1
        self.p2=p2
        self.game_over=False

    def start_dialogue(self,p1,opponent):
        print(f"A wild enemy has apppeared\n")
        
    def turn(self,p1,opponent):
        """Starts the turns of P1. It gives user option to surrender or attack.
        They can select a skill to attack with.
        
        Args:
            p1 (object): Player 1
            opponent (object): opponent of Player 1
        """    
        choice=input("1(Attack) or 2(Surrender)\n")
        if choice=="1":
            p1.select_skill()
            dmg=p1.damage()
            opponent.health-=dmg
            print(f"{p1.name} used {p1.skill}")
            print(f"{p1.name} caused {dmg} damage to {opponent.name}")
        elif choice=="2":
            game.surrender(p1)
            
    def monster_turn(self,monster,p1):
        """Monster's turn to randomly select a skill and affect users health 
        points
        
        Args:
            monster (object): monster object
            p1 (object): Player 1
        """
        monster.select_skill()
        dmg=monster.damage()
        p1.health-=dmg
        print(f"{monster.name} used {monster.skill}")
        print(f"{monster.name} caused {dmg} damage to {p1.name}")
        
    def display_hp(self,p1,p2):
        """It display the hp value of p1 and p2

        Args:
            p1 (Object): Player 1
            p2 (Object): Player 2 (monster)
        """
        print(f"\n------NEW HEALTH STATUS------\n"
              f"{p1.name}'s health = {p1.health}\n"
              f"{p2.name}'s health = {p2.health}\n"
              "-------------------------------\n")
        
    def check_win(self, player, opponent):
        """Checks if the hp values reaches 0 and draws a conclusion

        Args:
            player (Object): Player 1
            opponent (Object): Opponent of player 1
        """
        if player.health <= 0 and opponent.health > 0:
            self.game_over = True
            print("You Lose")
        elif opponent.health <= 0 and player.health > 0:
            self.game_over = True
            print("You Win")
        elif player.health <= 0 and opponent.health <= 0:
            self.game_over = True
            print("Draw")
            
    def surrender(player):
        """Allow the user to exit the game or surrender

        Args:
            player (player): The player
        """
        options ="N"
        options = str(input(f"{player.name}, do you wish to surrender?(Yes or No)\n"))
        if options.lower()in["yes"] or options.lower()in["y"]:
            print("The game will exit now")
            exit()
        elif options.lower()in["no"] or options.lower()in["n"]:
            pass

def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect two required arguments (the names of two players).
    
    Returns:
        namespace: a namespace with two attributes: name0 and name1, both
        strings.
    """
    parser = ArgumentParser(description='Begin playing the game')
    parser.add_argument('player', type=str, help="name of user")
    parser.add_argument('turn', type=int, help="an action user chooses")
    parser.add_argument('skill', type=int, help="skill choosen for attack")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    name1=input("Welcome to a Turn based RPG stimulation\n"
                "Please enter your name: ")
    p1=player(name1,"Sword Slash","Sword Dash") 
    m1=monster("Goblin","Goblin Bash","Goblin Strike")
    m2=monster("Evil Spirit","Spirit Attack","Spirit Dash")
    m3=monster("Dark Magician","Dark Magic","Dark Fireball")
    monsters=[m1,m2,m3]
    nextBattle='Yes'
    while nextBattle.lower() in ['y', 'yes']:
        random_monster=random.choice(monsters)
        g1=game(p1,random_monster)
        while g1.game_over == False:
            print(f"{p1.name}'s Turn: ")
            g1.turn(p1,random_monster)
            print(f"{random_monster.name}'s Turn: ")
            g1.monster_turn(random_monster,p1)
            g1.display_hp(p1,random_monster)
            g1.check_win(p1,random_monster)
        else:
            nextBattle=input("Do you want to move onto the next battle:(Yes or No)")
    else:
        if nextBattle.lower() in ['n', 'no']:
            exit()        
    
