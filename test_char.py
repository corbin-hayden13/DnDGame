import DnDCharacter as dndChar

def main():
    charOne = dndChar.DnDCharacter("0", "m", True, ["druid", "sorcerer", "barbarian"], [7, 11, 1])
    print(charOne)
    file_name = charOne.export()

    charTwo = dndChar.import_save("character_files/" + file_name)
    print(charTwo)


if __name__ == "__main__":
    main()

