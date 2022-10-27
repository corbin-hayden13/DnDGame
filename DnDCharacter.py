import copy
import random as rand
import sys
import fantasy_name_generator as fng
import regex as re

# Constants
class_list = ["sorcerer", "wizard", "artificer", "bard", "cleric", "druid", "monk", "rouge", "warlock",
                      "fighter", "paladin", "ranger", "barbarian"]

class DnDCharacter():
    """ Class hit dice:
    sorcerer, wizard = d6
    artificer, bard, cleric, druid, monk, rouge, warlock = d8
    fighter, paladin, ranger = d10
    barbarian = d12
    """
    def __init__(self, name, gender, rolling, char_classes, levels):
        if len(char_classes) != len(levels):
            sys.exit(1)

        self.char_classes = char_classes # a list of classes
        self.levels = levels # A list of levels
        self.hit_dice = []

        # Determine hit dice for classes
        dSixClasses = ["sorcerer", "wizard"]
        dEightClasses = ["artificer", "bard", "cleric", "druid", "monk", "rouge", "warlock"]
        dTenClasses = ["fighter", "paladin", "ranger"]
        # dTwelveClasses = ["barbarian"]

        for class_name in char_classes:
            if dSixClasses.count(class_name) == 1:
                self.hit_dice.append(6)

            elif dEightClasses.count(class_name) == 1:
                self.hit_dice.append(8)

            elif dTenClasses.count(class_name) == 1:
                self.hit_dice.append(10)

            else:  # Just default to barbarian, don't want to do error correction right now
                self.hit_dice.append(12)

        # Initialize more class variables
        # strength, dexterity, constitution, intelligence, wisdom, charisma
        self.character_stats = []

        # Roll for the stats
        for a in range(6):
            if rolling:
                self.character_stats.append(self.__roll_stat())

            else:
                self.character_stats.append(0)

        # Need to add multiclassing functionality to health modifier here
        self.health = self.__multiclass_health()
        # One nice line to initialize self.name of the object
        self.name = name if name != "0" else self.__get_rand_name(gender)
        self.gender = gender


    def __str__(self):
        padding = " "

        ret_str = self.name + ":\n"
        ret_str += "Classes:\n"
        for char_class in range(len(self.char_classes)):
            ret_str += padding + self.char_classes[char_class]
            ret_str += " Lvl " + str(self.levels[char_class]) + "\n"

        ret_str += "Strength Modifier: " + str(self.__calc_stat_mod(self.character_stats[0])) + "\n"
        ret_str += "Dexterity Modifier: " + str(self.__calc_stat_mod(self.character_stats[1])) + "\n"
        ret_str += "Constitution Modifier: " + str(self.__calc_stat_mod(self.character_stats[2])) + "\n"
        ret_str += "Intelligence Modifier: " + str(self.__calc_stat_mod(self.character_stats[3])) + "\n"
        ret_str += "Wisdom Modifier: " + str(self.__calc_stat_mod(self.character_stats[4])) + "\n"
        ret_str += "Charisma Modifier: " + str(self.__calc_stat_mod(self.character_stats[5])) + "\n"

        ret_str += "\nHealth: " + str(self.health) + "\n"

        return ret_str


    # This is for writing the character to a file for later import
    def export(self):
        file_name = self.name.replace(" ", "_") + ".txt"
        out_file = open("character_files/" + file_name, "w")
        out_file.write(self.name.replace(" ", "_") + "_" + self.gender + "\n")

        """ Write classes and levels of charater """
        for char_class in range(len(self.char_classes)):
            out_str = str(class_list.index(self.char_classes[char_class]))  # return number instead of writing string
            out_str += ":"  # Acts as known delimiter
            out_file.write(out_str)

        out_file.write("\n")

        for level in self.levels:
            out_str = str(level) + ":"  # Acts as known delimiter
            out_file.write(out_str)

        """ Write character_stats """
        out_file.write("\n")
        out_str = ""
        for stat in self.character_stats:
            out_str += str(stat) + ":"

        out_file.write(out_str)

        return file_name


    def roll_check(self, roll_type, proficiency=False, expertise=False, advantage=-1):
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
            modifier = self.__calc_stat_mod(self.character_stats[0])

        elif dexterity_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.character_stats[1])

        elif intelligence_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.character_stats[3])

        elif wisdom_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.character_stats[4])

        elif charisma_check.count(check_type) == 1:
            modifier = self.__calc_stat_mod(self.character_stats[5])

        # Because higher roll is rolls[0], if advantage use higher roll, if disadvantage use rolls[1]
        if advantage > -1:
            rolls = [rand.randint(1, 20), rand.randint(1, 20)]
            rolls.sort(reverse=True)

            return rolls[advantage] + modifier + (proficiency * (2 if expertise else 1))

        return rand.randint(1, 20) + modifier + (proficiency * (2 if expertise else 1))


    # This is the template for future saving throws
    # def saving_throws(self, proficiency=0):

    def get_name(self):
        return self.name


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


    def set_stats(self, lst_char_stats):
        self.character_stats = copy.deepcopy(lst_char_stats)
        self.health = self.__multiclass_health()


    def __get_health(self, char_level, hit_dice_val):
        total_health = 0

        const_modifier = (self.character_stats[0] - 10) // 2
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


    def __get_rand_name(self, gender):
        if gender == "M" or gender == "m":
            return fng.get_male_name()
        else:
            return fng.get_female_name()


def import_save(file_path):
    save_file = open(file_path, "r")
    file_lines = save_file.readlines()

    temp_name = list(file_lines[0].split("_"))
    name = temp_name[0] + " " + temp_name[1]
    gender = temp_name[2]

    char_classes = list(file_lines[1].split(":"))
    char_classes.pop()  # Because \n will most likely be the last element of the list
    for char_class in range(len(char_classes)):  # Converting class number to string name
        char_classes[char_class] = class_list[int(char_classes[char_class])]

    levels = list(file_lines[2].split(":"))
    levels.pop()
    for level in range(len(levels)):
        levels[level] = int(levels[level])

    temp_char = DnDCharacter(name, gender, False, char_classes, levels)
    temp_stats = list(file_lines[3].split(":"))
    temp_stats.pop()
    for stat in range(len(temp_stats)):
        temp_stats[stat] = int(temp_stats[stat])

    temp_char.set_stats(temp_stats)

    return temp_char

