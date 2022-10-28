class CharacterClass:
    op_skills_prof_list = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
                           'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance',
                           'Persuasion',
                           'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

    def __init__(self, name, hit_dice, saving_throws, armor_prof, weapon_prof, tool_prof, skill_prof):
        self.name = str(name).lower()
        self.hit_dice = int(hit_dice)
        self.armor_prof = list(armor_prof)
        self.weapon_prof = list(weapon_prof)
        self.tool_prof = list(tool_prof)
        self.skill_prof = list(skill_prof)
        self.saving_throws = list(saving_throws)


    def add_saving_throws(self, list_of_throws):
        self.saving_throws.append(list(list_of_throws))

    @classmethod
    def make_skill_profs_list(prof_list):
        num_profs = 2
        out_list = []

        for prof_org in op_skills_prof_list:
            found = False
            for prof_curr in prof_list:
                if prof_org == prof_curr:
                    out_list.append(num_profs)
                    found = True

            if not found:
                out_list.append(0)

        return out_list




class Sorcerer(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self, "sorcerer", 6, ["constitution", "charisma"], [], [], [],
                                [0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0])


class Wizard(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self, "wizard", 6, ["intelligence", "wisdom"], [], [], [],
                                [0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0])


class Artificer(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self, "artificer", 8, ["intelligence", "constitution"], [], [], [],
                                [0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0])


# Bard chooses from 3 proficiencies
class Bard(CharacterClass):
    def __init__(self, list_of_skills):
        CharacterClass.__init__(self, "bard", 8, ["charisma", "dexterity"], [], [], [],
                                CharacterClass.make_skill_profs_list(list_of_skills))


class Cleric(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self, "cleric", 8, ["wisdom", "charisma"], [], [], [],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


class Druid(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self, "druid", 8, ["intelligence", "wisdom"], [], [], [],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


class Monk(CharacterClass):
    def __init__(self, lvl):
        if int(lvl) >= 14:
        CharacterClass.__init__(self, "monk", 8, ["dexterity", "strength", "constitution", "charisma", "wisdom", "intelligence"], [], [], [],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    else:
        CharacterClass.__init__(self, "monk", 8, ["dexterity", "strength"], [], [], [],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


# Rogue chooses from 4 proficiencies
class Rogue(CharacterClass):
    def __init__(self, list_of_skills):
        CharacterClass.__init__(self, "rogue", 8, ["dexterity", "intelligence"], [], [], []
                                CharacterClass.make_skills_prof_list(list_of_skills))


class_list = [CharacterClass("monk",      8,  ["dexterity", "strength", "constitution", "charisma", "wisdom", "intelligence"],
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

""" I've got a long way to go before I can start making custom classes
def add_cust_class(name, hit_dice, saving_throws):
    new_char_class = name.lower()
    # Make sure this is not an existing class
    for char_class in range(len(class_list)):
        if new_char_class == class_list[char_class]:
            print(new_char_class + " is already a class.")
            return 1  # Failed custom class add

    class_list.append(CharacterClass(new_char_class, hit_dice, saving_throws))
    return 0  # Successful custom class add
"""

def get_char_class(class_name):
    for char_class in range(len(class_list)):
        if class_name == class_list[char_class].name:
            return class_list[char_class]  # returns a CharacterClass object for reference
