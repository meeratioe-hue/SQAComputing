from dataclasses import dataclass
@dataclass
class orders():
    orderNum : str =""
    date: str =""
    email : str =""
    option : str =""
    cost : float = 0.0
    rating : int = 0

finalorders = [orders() for i in range(505)] #array of records

def ReadFromFileIntoArrayOfRecords():
#read data from the ‘orders.txt’ file and store into an array of records
    with open ("orders.txt") as readfile:
        nextLine = readfile.readline().rstrip("\n")
        for i in range (505):
            items = nextLine.split(",")
            finalorders[i].orderNum = items[0]
            finalorders[i].date = items[1]
            finalorders[i].email = items[2]
            finalorders[i].option = items[3]
            finalorders[i].cost = float(items[4])
            finalorders[i].rating = int(items[5])
            nextLine = readfile.readline().rstrip("\n")
            ##finalorders is an array. take first thing from that and set it to orderNum in orders
    return finalorders 

def FindThePositionOfTheCustomer(finalorders) :
#2.1 Set position to -1
    position = -1 
#2.2 Set index to 0
    index = 0
#2.3 Ask user to enter month to search for
    month = input("Enter the first three letters of the month to search: ")
#2.4 While position is -1 and index is less than the length of the array
    while position == -1 and index < 505:
#2.5 If current month is equal to searched month and current rating is 5 then
        if finalorders[index].date[3:6] == month and finalorders[index].rating == 5:
#2.6 Set position to index
            position = index 
#2.7 End if
#2.8 Add 1 to index
        index = index + 1
#2.9 End while
#2.10 Return position
    return position 

def WriteDetailsOfTheWinningCustomer (finalorders, position):
#3.1 Open new file ‘winningCustomer.txt’
    with open("winningCustomer.txt", "w") as writefile:
#3.2 If position is 0 or above then
        if position >= 0 :
#3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
                writefile.write(finalorders[position].orderNum + "," + finalorders[position].email + "," +  str(finalorders[position].cost))
#3.4 Else
        else:
#3.5 Write ‘No winner’ to ‘winningCustomer.txt’
            writefile.write("No winner")
#3.6 End if
#3.7 Close ‘winningCustomer.txt’

def DisplayTheTotalNumberOfOrders (finalorders):
#4.1 Call countOption function to return the number of orders delivered
    countOption(finalorders)
#4.2 Call countOption function to return the number of orders collected
#4.3 Output the total number of orders delivered
print("Total number of orders delivered to date: ", counterDelivered)
#4.4 Output the total number of orders collected
print("Total number of orders collected to date: ", counterCollected)

def countOption (finalorders):
    counterDelivered = 0
    counterCollected = 0 
    for i in range(len(finalorders)):
        if finalorders[i].option == "Delivery":
            counterDelivered = counterDelivered + 1
        elif finalorders[i].option == "Collection":
            counterCollected = counterCollected + 1
        else:
            counterDelivered = counterDelivered
            counterCollected - counterCollected

#main program
finalorders=ReadFromFileIntoArrayOfRecords()
position = FindThePositionOfTheCustomer(finalorders)
WriteDetailsOfTheWinningCustomer (finalorders, position)
DisplayTheTotalNumberOfOrders (finalorders)

#notes:
#array stores one type 
#record stores a bunch of things
#with open (path="orders.txt") DO THIS IF GOT ERROR (Ex. in github)
#print has to be in line 68 and 70 instead of line 83 and 84 cos of comments 4.3 and 4.4 