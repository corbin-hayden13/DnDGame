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
import DnDCharacter

# This is a CharacterManager, not a creator (because DnDCharacter does this already)

class CharacterManager:
    def __init__(self, character_list=[]):
        self.character_list = character_list

    def new_character(self, list_of_stats):
        # Create a new character object from a list of the parameters to pass
        # self.character_list.append(new DnDCharacter())

    def import_character(self, file_path):
        # Read in a character file and create a new character object from it

"""
numCharacters = 8
numStats = 6
num_extra_modifiers = 4 # Used for sys.argv list offset, includes program name (so modifiers plus 1)

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

    dnd_character_one = DnDCharacter(name, gender, rolling, classes, levels)

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

    # This is a test of the git push and pull within linux terminal on iPad
    sys.exit(main())
"""
