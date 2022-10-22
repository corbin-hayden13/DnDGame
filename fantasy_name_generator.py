from random import randrange

def __line_appender(file_path, target):
    file = open(file_path, "r")
    splitfile = file.read().splitlines()
    for line in splitfile:
        target.append(line)


def __name_selector(target_list):
    selected = target_list[randrange(len(target_list))]

    return selected


def __name_builder(first_name_list_path, last_name_list_path):
    first_name_list = []
    last_name_list = []

    __line_appender(first_name_list_path, first_name_list)
    __line_appender(last_name_list_path, last_name_list)

    first_name_selected = __name_selector(first_name_list)
    last_name_selected = __name_selector(last_name_list)

    name = first_name_selected + " " + last_name_selected

    return name


def get_male_name():
    return __name_builder("first_name_male.txt", "last_name.txt")

def get_female_name():
    return __name_builder("first_name_female.txt", "last_name.txt")