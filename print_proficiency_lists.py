op_skills_prof_list = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
                'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
                'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

def print_skill_profs(prof_list):
    num_profs = 2
    out_str = "["

    for prof_org in op_skills_prof_list:
        found = False
        for prof_curr in prof_list:
            if prof_org == prof_curr:
                out_str += str(num_profs) + ", "
                found = True

        if not found:
            out_str += "0, "

    out_str = out_str[:len(out_str) - 2]
    out_str += "]"

    print(out_str)


def main():
    print_skill_profs(['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'])


if __name__ == "__main__":
    main()

