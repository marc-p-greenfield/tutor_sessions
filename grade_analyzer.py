def mean(list):
    total = sum(list)
    length = len(list)
    print ("Mean grade is : ", str(total/length))

def median(list):
    n = len(list)
    median = 0
    if n < 1:
            return None
    if n % 2 == 1:
            median = sorted(list)[n//2]
    else:
            median = sum(sorted(list)[n//2-1:n//2+1])/2.0
    print ("Median grade is : ", str(median))

def mode(list):
    num_dict = {}
    for i in list:
        if i in num_dict.keys():
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    max_list = []
    max_count = 0
    for k in num_dict:
        if num_dict[k] > max_count:
            max_count = num_dict[k]
            max_list = [k]
        elif num_dict[k] == max_count:
            max_list.append(k)
    print ("Mode grade(s): " + str(max_list)[1:-1] + " occured " + str(max_count) + " time(s) each.")

number_list = []
file = open("data.txt")
for x in file:
    number_list.append(int(x))

mean(number_list)
median(number_list)
mode(number_list)
