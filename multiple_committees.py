from committee_combinations import committee

professors = int(input("Enter the number of professors in the department"))
prof_on_multiple_committees = input("Can a professor be on multiple committees? Enter y or n:")
free_profs = professors
total_combinations = 1

if prof_on_multiple_committees == 'y':
    bool_prof_on_multiple_committees = True
else:
    bool_prof_on_multiple_committees = False

while True:
    committee_name = input("Enter the name of the committee:")
    if committee_name == "":
        break
    committee_chair_person = input("Does the committee need a chair? Enter y or n:")
    if committee_chair_person == 'y':
        bool_chair = True
    else:
        bool_chair = False
    number_of_members = int(input("How many members?"))
    if number_of_members > free_profs:
        combos = committee(free_profs, number_of_members, bool_chair)
        print("Assigning only", free_profs, "members to the", committee_name, "committee.")
        print("there are", combos, "ways to form the", committee_name, "commitee.")
        total_combinations = total_combinations * combos
        free_profs = 0
        break
    else:
        combos = committee(free_profs, number_of_members, bool_chair)
        print ("There are", combos, "ways to form the", committee_name, "committee.")
        total_combinations = total_combinations * combos
        if bool_prof_on_multiple_committees == False:
            free_profs = free_profs - number_of_members
    if bool_prof_on_multiple_committees == False and free_profs == 0:
        break

print ("There are", total_combinations, "ways to form all the committees")
