#Function to remove a value from a list based on an index
def myPop(alist,index):
    #Creates a new list to work with
    new_list = []
    i = 0
    #Iterates through the list
    while i < len(alist):
        #Checks to see if the current index is equal to the specified one, if so, does not append to new_list.
        #If the index is different, it appends the value to the new_list
        if i == index:
            i += 1
            pass
        else:
            new_list.append(alist[i])
            i += 1
    return new_list

#Function to remove an item from a list
def myRemove(alist, item):
    new_list = []
    #Iterates through the list checking to see if the current item is equal to the item specified.
    #If so, does not append to the new list, if not it appends it
    for i in alist:
        if i == item:
            pass
        else:
            new_list.append(i)
    return new_list

#Function to search through a dictionary and remove an entry based on the key
def dictPop(adict,key):
    new_dict = {}
    #Iterates through a dictionary looking for a specified key and removes the entry if found
    for i in adict:
        if i == key:
            pass
        else:
            new_dict[i] = adict[i]
    return new_dict

#Function to remove an entry from a dictionary basd on the value
def dictRemove(adict,value):
    new_dict = {}
    #Iterates through the dictionary checking if the current value is the value we are looking for.
    #If so, does not add it to the new dictionary
    for i in adict:
        if adict[i] == value:
            pass
        else:
            new_dict[i] = adict[i]
    return new_dict

#Function to insert specificed item at a certain index
def insert(alist, item, index):
    new_list = []
    for counter in range(len(alist)):
        if counter == index:
            new_list.append(item)
            for new_counter in alist[counter:]:
                new_list.append(new_counter)
                break
        else:
            new_list.append(alist[counter])
    return new_list

#Function to remove nested lists in a list
def flatten(alist):
    new_list = []
    for lists in alist:
        for items in lists:
            new_list.append(items)
    return new_list
