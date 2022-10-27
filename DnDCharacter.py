import random as rand
import sys
import fantasy_name_generator as fng
import regex as re

# Constants
numCharacters = 8
numStats = 6
num_extra_modifiers = 4 # Used for sys.argv list offset, includes program name (so modifiers plus 1)

class DnDCharacter():
    """ Class hit dice:
    sorcerer, wizard = d6
    artificer, bard, cleric, druid, monk, rouge, warlock = d8
    fighter, paladin, ranger = d10
    barbarian = d12
    """
    def __init__(self, name, gender, rolling, char_classes, levels):
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
        # One nice line to initialize self.name of the object
        self.name = name if name != "0 " else get_rand_name(gender)


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

    
    """ @classmethod
    def import(file_path):
        # Reading character file to new character

    """

    # This is for writing the character to a file for later import
    def export(self):
        out_file = open("Char_" + self.name.replace(" ","") + "_Out.txt", "w")
        out_file.write(self.name)
        for char_class in range(len(self.char_classes)):
            out_str = self.char_classes[char_class]
            out_str += ":" + str(self.levels[char_class])
            out_file.write(out_str)


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


    def __get_rand_name(self, gender):
        if gender == "M" or gender == "m":
            return fng.get_male_name()
        else:
            return fng.get_female_name()


def new_character(name, gender, rolling, classes, levels):
    return DnDCharacter(name, gender, rolling, classes, levels)
