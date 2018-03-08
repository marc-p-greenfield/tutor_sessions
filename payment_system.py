number_of_employees = int(input("How many employees do you want to enter:"))
total_payment = 0

for i in range(number_of_employees):
    name = input('Please enter name: ')
    hours = float(input('How many hours did you work this week? '))
    rate = float(input('What is your hourly rate?'))

    payment = 0
    overtime = 0

    if hours > 40:
        overtime = hours - 40
        hours = 40

    payment = (hours * rate) + (overtime * rate * 1.5)
    total_payment += payment

    print(name)
    print("${:,.2f}".format(payment))

print (total_payment)
print (total_payment/number_of_employees)
