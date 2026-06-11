items = []
names = []
marks = []
with open("pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
#example: line "emelia, 24"
    while line:
        items = line.split(",")
        #get a line, and split it into "emelia" and "24"
        names.append(items[0])
        #take the name and add to a table of sorts. index 0 cos "emelia" 
        # is the first thing within line 6
        marks.append(items[1])
        #add "24" to a different table
        line = readfile.readline().rstrip('\n')
        # continue reading


#remember: append means add to the end of
#while means while the file is open 