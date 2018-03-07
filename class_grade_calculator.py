#****************** LAB Average  ******************
def labAvg(infile):
    g1 = int(infile.readline())
    g2 = int(infile.readline())
    g3 = int(infile.readline())
    g4 = int(infile.readline())
    g5 = int(infile.readline())
    g6 = int(infile.readline())
    g7 = int(infile.readline())

    print("Lab Grades:",g1,g2,g3,g4,g5,g6,g7)

    sum = g1+g2+g3+g4+g5+g6+g7
    avg = sum / 7    # computes avg
    avg = avg / 10   # computes % (because labs are worth 10 points)

    return avg

#****************** PA Average  ******************
def paAvg(infile):
    g8 = int(infile.readline())
    g9 = int(infile.readline())
    g10 = int(infile.readline())

    print("PAs:", g8,g9,g10)

    sum2 = g8+g9+g10
    avg2 = sum2 / 3
    avg2 = avg2 / 100

    return avg2
#****************** EXAM Average  ******************
def exAvg(infile):
    g11 = int(infile.readline())

    print("Exam:",g11)

    return g11/100

#****************** MAIN/DRIVER  ******************
def main():
    # main will call each of your average functions
    # to compute each components of overall class avg
    # call the function to compute your LAB average
    # put the return value in the variable labAverage

    infile = open("temp_data.txt",'r')
    labAverage = labAvg(infile)

    # call the function to compute your PA average
    paAverage = paAvg(infile)

    # call the function to computer your EXAM average
    exAverage = exAvg(infile)

    # close the file
    infile.close()

    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet
    overallAverage = (labAverage*10) + (paAverage*15) + (exAverage*75)


    # print results
    print("  Lab Average =", labAverage*100,"%")
    print("   PA Average =","%.2f"% (paAverage*100),"%")
    print(" Exam Average =","%.2f"% (exAverage*100),"%")
    print("-------------")
    print("Class Average =","%.2f"% (overallAverage),"%")

main()
