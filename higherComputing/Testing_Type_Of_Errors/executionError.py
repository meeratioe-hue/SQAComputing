#execution error :
#is an error that only becomes evident during run time.
#in this example, "1101 Task 7" doesn't exist



#-------------Main Program-----------------
#open file
import time
with open("1101. File Handling/1101 Task 7/SampleFile.txt") as readfile:
    #filecontents = readfile.read()
    nextLine = readfile.readline()
    while nextLine != "":
        print(nextLine.strip())
        time.sleep(2)
        nextLine = readfile.readline()




