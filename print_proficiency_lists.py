op_skills_prof_list = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
                'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
                'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

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

    print(out_list)

    return out_list


def main():
    make_skill_profs_list(['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'])


if __name__ == "__main__":
    main()

