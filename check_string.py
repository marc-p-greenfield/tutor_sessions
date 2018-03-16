#Define a function that will take in two strings as its arguments
def makeStr(string1, string2):
#Declare a boolean variable that we will update later to print proper result
    bool_check = True
    #Create a loop to check each character within string2
    for x in range(len(string2)):
        #Catch if a character in string2 is not in string1
        #This is case insensitive - to make it case sensitive just remove .upper and .lower and just check string2[x]
        if string2[x].upper() and string2[x].lower() not in string1:
            #Set our bool_check to false to use later
            bool_check = False
            #We don't want to continue checking because we have a negative so end the fxn
            break
        else:
            #If each character from string2 is in string1, bool_check will stay true
            bool_check = True
    #Use this if/else check to check bool_true and print "YES" or "NO" depending
    if bool_check == True:
        print ("YES")
    else:
        print ("NO")

#Sample calls
makeStr("hello", "")
makeStr("hello", "olleloheloeloheloel")
makeStr("hello", "olleloheloteloheloel")
