class CharacterClass:
    def __init__(self, name, hit_dice):
        self.name = str(name).lower()
        self.hit_dice = int(hit_dice)


class Sorcerer(CharacterClass):
    def __init__(self):
        CharacterClass.__init__("sorcerer", 6)
        self.armor_prof = []
        self.weapon_prof = []
        self.tool_prof = []
        self.skill_prof = [0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0]
        self.saving_throws = []


class Wizard(CharacterClass):
    pass  # Look into using this method more
    CharacterClass.__init__("wizard", 6)


class_list = [CharacterClass("sorcerer",  6,  ["constitution", "charisma"],
                             [0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0]),
              CharacterClass("wizard",    6,  ["intelligence", "wisdom"],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
              CharacterClass("artificer", 8,  ["intelligence", "constitution"],
                             [0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0]),
              # implement pick 3 skills for bard
              CharacterClass("bard",      8,  ["charisma", "dexterity"],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
              CharacterClass("cleric",    8,  ["wisdom", "charisma"],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
              CharacterClass("druid",     8,  ["intelligence", "wisdom"],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
              CharacterClass("monk",      8,  ["dexterity", "strength", "constitution", "charisma", "wisdom", "intelligence"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2]),
              CharacterClass("rogue",     8,  ["dexterity", "intelligence"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2]),
              CharacterClass("warlock",   8,  ["wisdom", "charisma"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2]),
              CharacterClass("fighter",   10, ["strength", "constitution"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2]),
              CharacterClass("paladin",   10, ["wisdom", "charisma"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2]),
              CharacterClass("ranger",    10, ["dexterity", "strength"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2]),
              # CharacterClass("blood hunter", 10, ["dexterity", "intelligence"],
              #                              [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2]),
              CharacterClass("barbarian", 12, ["strength", "constitution"],
                             [0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2])]


def add_cust_class(name, hit_dice, saving_throws):
    new_char_class = name.lower()
    # Make sure this is not an existing class
    for char_class in range(len(class_list)):
        if new_char_class == class_list[char_class]:
            print(new_char_class + " is already a class.")
            return 1  # Failed custom class add

    class_list.append(CharacterClass(new_char_class, hit_dice, saving_throws))
    return 0  # Successful custom class add


def get_char_class(class_name):
    for char_class in range(len(class_list)):
        if class_name == class_list[char_class].name:
            return class_list[char_class]  # returns a CharacterClass object for reference
