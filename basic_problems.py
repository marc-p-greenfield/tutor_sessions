filenames = ["all-the-single", "call-me-maybe"]

for file_name in (filenames):
    print (file_name.replace("-", " "))


def convert_fahrenheit(temperature):
    Fahrenheit = (temperature*9/5) + 32
    return Fahrenheit

temperatures = [10,20,30]
for item in temperatures:
    print(convert_fahrenheit(item))

def average(a_list):
    count = 0
    for item in a_list:
        count = count + 1
    sum = 0
    for item in a_list:
        sum = sum + item
    average = sum/count
    return average
print(average([10,7,10]))
