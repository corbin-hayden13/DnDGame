"""
command +:wq to save and quit
i to enter insert mode

Hayden Corbin
Used to determine stats based on dice rolls for DnD
"""

"""
Constitution modifier
score - 10 // 2 = modifier, caps at 30 = +10

Roll class hit dice for # times = level
dice values + constitution modifier

Parameters:
Const score
Class hit dice
Level

Class hit dice:
sorcerer, wizard = d6
artificer, bard, cleric, druid, monk, rouge, warlock = d8
fighter, paladin, ranger = d10
barbarian = d12
"""

import random as rand
import sys
import fantasy_name_generator as fng
import regex as re

# Constants
numCharacters = 8
numStats = 6
num_extra_modifiers = 4 # Used for sys.argv list offset, includes program name (so modifiers plus 1)

class DnD_Character():
    """ Class hit dice:
    sorcerer, wizard = d6
    artificer, bard, cleric, druid, monk, rouge, warlock = d8
    fighter, paladin, ranger = d10
    barbarian = d12
    """
    def __init__(self, name, gender, rolling, char_classes, levels):
        self.name = name
        self.char_classes = char_classes # a list of classes
        self.levels = levels # A list of levels
        self.hit_dice = []

        # Determine hit dice for classes
        dSixClasses = ["sorcerer", "wizard"]
        dEightClasses = ["artificer", "bard", "cleric", "druid", "monk", "rouge", "warlock"]
        dTenClasses = ["fighter", "paladin", "ranger"]

        for class_name in char_classes:
            if dSixClasses.count(class_name) == 1:
                self.hit_dice.append(6)

            elif dEightClasses.count(class_name) == 1:
                self.hit_dice.append(8)

            elif dTenClasses.count(class_name) == 1:
                self.hit_dice.append(10)

            elif class_name != "barbarian":
                sys.exit()

            else:
                self.hit_dice.append(12)

        # Initialize more class variables
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

        # Roll for the stats
        if rolling:
            self.strength = self.__roll_stat()
            self.dexterity = self.__roll_stat()
            self.constitution = self.__roll_stat()
            self.intelligence = self.__roll_stat()
            self.wisdom = self.__roll_stat()
            self.charisma = self.__roll_stat()

        # Need to add multiclassing functionality to health modifier here
        self.health = self.__multiclass_health()


    def __str__(self):
        padding = " "

        ret_str = self.name + ":\n"
        ret_str += "Classes:\n"
        for char_class in range(len(self.char_classes)):
            ret_str += padding + self.char_classes[char_class]
            ret_str += " Lvl " + str(self.levels[char_class]) + "\n"

        ret_str += "Strength Modifier: " + str(self.__calc_stat_mod(self.strength)) + "\n"
        ret_str += "Dexterity Modifier: " + str(self.__calc_stat_mod(self.dexterity)) + "\n"
        ret_str += "Constitution Modifier: " + str(self.__calc_stat_mod(self.constitution)) + "\n"
        ret_str += "Intelligence Modifier: " + str(self.__calc_stat_mod(self.intelligence)) + "\n"
        ret_str += "Wisdom Modifier: " + str(self.__calc_stat_mod(self.wisdom)) + "\n"
        ret_str += "Charisma Modifier: " + str(self.__calc_stat_mod(self.charisma)) + "\n"

        ret_str += "\nHealth: " + str(self.health) + "\n"

        return ret_str

    def roll_check(self, roll_type, proficiency=0, expertise=False, advantage=-1):
        # Proficiency is added onto roll
        # Expertise doubles proficiency
        # advantage (-1) = nothing
        # advantage (0) = roll twice, use higher of two rolls
        # disadvantage (1) = roll twice, keep lower of two rolls

        dexterity_check = ["acrobatics", "sleight of hand", "stealth"]
        intelligence_check = ["arcana", "history", "investigation", "nature", "religion"]
        wisdom_check = ["insight", "medicine", "animal handling", "perception", "survival"]
        charisma_check = ["intimidation", "deception", "performance", "persuasion"]

        check_type = roll_type.lower()
        modifier = 0

        if check_type == "athletics":
            modifier = self.__calc_stat_mod(self.strength)

        elif dexterity_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.dexterity)

        elif intelligence_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.intelligence)

        elif wisdom_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.wisdom)

        elif charisma_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.charisma)

        # Because higher roll is rolls[0], if advantage use higher roll, if disadvantage use rolls[1]
        if advantage > -1:
            rolls = [rand.randint(1, 20), rand.randint(1, 20)]
            rolls.sort(reverse=True)

            return rolls[advantage] + modifier + (proficiency * (2 if expertise else 1))

        return rand.randint(1, 20) + modifier + (proficiency * (2 if expertise else 1))


    # This is the template for future saving throws
    # def saving_throws(self, proficiency=0):


    def __calc_stat_mod(self, stat):
        return (stat - 10) // 2


    def __roll_stat(self):
        finalVal = 0
        listOfRolls = []

        for ab in range(4): # Discard values of 1 from D6, typically rerolled anyways
            listOfRolls.append(rand.randint(2, 6))

        # Need to add up the top three rolls
        listOfRolls.sort(reverse=True) # Sorts is descending order, not default ascending
        for bb in range(3): # Add up first three elements in list (greatest three numbers)
            finalVal += listOfRolls[bb]

        listOfRolls.clear()

        return finalVal


    def __get_health(self, char_level, hit_dice_val):
        total_health = 0

        const_modifier = (self.constitution - 10) // 2
        if const_modifier > 10:
            const_modifier = 10

        if const_modifier < -5:
            const_modifier = -5

        for rolls in range(char_level):
            total_health += rand.randint(const_modifier + 1, hit_dice_val + const_modifier)

        return total_health if total_health >= 1 else 1


    def __multiclass_health(self):
        total_health = 0
        for level in range(len(self.levels)):
            total_health += self.__get_health(self.levels[level], self.hit_dice[level])

        return total_health


def parse_class_args(classes_list=[], levels_list=[]):
    print("parsing args")
    # sys.argv[num_extra_modifiers + N] is class(es) and levels per class
    for char_class in range(num_extra_modifiers, num_extra_modifiers + ((len(sys.argv) - num_extra_modifiers) // 2)):
        classes_list.append(sys.argv[char_class])

    for level in range(num_extra_modifiers + ((len(sys.argv) - num_extra_modifiers) // 2), len(sys.argv)):
        levels_list.append(int(sys.argv[level]))


def main():
    classes_list = []
    levels_list = []
    # test character object
    # name, gender, rolling=True, classes, levels as the arguments passed to the script
    name = sys.argv[1]
    gender = sys.argv[2]
    rolling = bool(sys.argv[3])

    if (len(sys.argv) - num_extra_modifiers) % 2 == 1: # Number levels != number classes provided
        print("Number of levels != number of classes provided")

        return 1

    # sys.argv[num_extra_modifiers + N] is class(es) and levels per class
    parse_class_args(classes_list, levels_list)

    test_character = DnD_Character(name, gender, rolling, classes_list, levels_list)
    print(test_character)
    print("Roll investigation check:", test_character.roll_check("investigation", proficiency=2))

    return 0


def make_character():
    classes = []
    levels = []

    name = input("What is the name of your character? (0 for random name)")
    out_str = "Is your character male or female? (M / F)"
    gender = input(out_str)
    if name == "0":
        if gender == "M" or gender == "m":
            name = fng.get_male_name()
        else:
            name = fng.get_female_name()

    rolling = bool(input("Are you rolling for your stats? (True / False)"))
    out_str = "How many classes does " + name + " have?"
    num_classes = int(input(out_str))

    for a in range(num_classes):
        out_str = "What is class " + str(a + 1) + " of " + name + "?"
        classes.append(input(out_str).lower())

        out_str = "What is the level of " + name + "'s " + classes[a] + " class?"
        levels.append(int(input(out_str)))

    dnd_character_one = DnD_Character(name, gender, rolling, classes, levels)

    print(dnd_character_one)


# def game_loop():



def print_help():
    print("Using DnD character creator (By Hayden Corbin)")
    print("First argument is bool (True, False) is multiclassing")
    print("Next set of arguments is the hit dice (int, Ex. 6) corresponding to class type(s)")
    print("Final set of arguments is the level (int, Ex. 10) per class")
    print("Example run: python", sys.argv[0], "True 6 8 12 6")

    return 0


if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == "help":
        sys.exit(print_help())

    if len(sys.argv) == 1:  # Not using command line to run script
        make_character()


    sys.exit(main())