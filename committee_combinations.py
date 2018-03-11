def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of a negative number.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

def committee(people, members, chairperson = True):
    if people <= 0:
        raise ValueError("People count must be positive.")
    elif members > people:
        raise ValueError("Member count must not be greater than people count.")
    else:
        if chairperson == True:
            combos = (factorial(people)/(factorial(members-1)*factorial(people-members)))
            return int(combos)
        else:
            combos = (factorial(people)/(factorial(members)*factorial(people-members)))
            return int(combos)




print(committee(10, 3))
print(committee(10, 3, False))
print(committee(members = 3, people = 10, chairperson = True))
print(committee(chairperson = False, members = 3, people = 10))
print(committee(2, 2, True))
print(committee(3, 3, False))
