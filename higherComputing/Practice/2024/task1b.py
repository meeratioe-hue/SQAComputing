company_array = []
numEmployees_array = []
ceoSalary_array = []

#Read from file into parallel arrays
def ReadFromFileIntoParallelArrays():
    with open ("Practice/2024/companies.txt") as readfile:
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            company_array.append(items[0])
            numEmployees_array.append(items[1])
            ceoSalary_array.append(items[2])
            line = readfile.readline().rstrip('\n')
    return company_array, numEmployees_array, ceoSalary_array

# Find and display the difference between the chosen company's CEO salary
# and the highest CEO salary

def FindDifferenceBetweenCEOs(company_array, ceoSalary_array):
    companyAsked = input("Enter a company: ")
    found = False 
    maxi, position = findMaxPos(ceoSalary_array)
    for i in range (len(company_array)):
        if company_array[i] == companyAsked:
            found = True
            position = i
    if found == True:
        DifferenceBetweenSalaries = int(ceoSalary_array[position] - maxi)
        print("The company with the highest CEO salary is: " , company_array[i])
        print ("Chosen Company: ", companyAsked)
        print ("Difference between salaries: ", DifferenceBetweenSalaries)
    else:
        print("Company not found")

def findMaxPos(ceoSalary_array):
    maxi = ceoSalary_array[0]
    for i in range (len(ceoSalary_array)):
        if ceoSalary_array[i] > maxi:
            maxi = ceoSalary_array[i]
            position = i
    return maxi, position 


company_array,numEmployees_array, ceoSalary_array = ReadFromFileIntoParallelArrays()
FindDifferenceBetweenCEOs(company_array, ceoSalary_array)







"""
def FindDifferenceBetweenCEOs(company_array, ceoSalary_array):
# 2.1 Ask user to enter the name of chosen company
    companyAsked = input("Enter a company: ")
# 2.2 Set found to false
    found = False 
# 2.3 Call findMaxPos function to return the position of highest CEO salary
    maxi, position = findMaxPos(ceoSalary_array)
# 2.4 Loop for company array
    for i in range (len(company_array)):
# 2.5   If current company is the chosen company
        if company_array[i] == companyAsked:
# 2.6        Set found to true
            found = True
# 2.7       Set position to current index
            position = i
# 2.8 End if
# 2.9 End loop

# 2.10 If chosen company name is in list
    if found == True:
# 2.11   Subtract and store chosen company’s CEO salary from highest CEO salary
        DifferenceBetweenSalaries = int(ceoSalary_array[position] - maxi)
# 2.12   Display message containing name of company with highest CEO salary, name of chosen company, and difference in salaries
        print("The company with the highest CEO salary is: " , company_array[i])
        print ("Chosen Company: ", companyAsked)
        print ("Difference between salaries: ", DifferenceBetweenSalaries)
# 2.13 Else
    else:
# 2.14  Display “Company not found”
        print("Company not found")
# 2.15 End if

def findMaxPos(ceoSalary_array):
    maxi = ceoSalary_array[0]
    for i in range (len(ceoSalary_array)):
        if ceoSalary_array[i] > maxi:
            maxi = ceoSalary_array[i]
            position = i
    return maxi, position 


#Find and display the highest number of employees employed by a single
#company and the number of companies who employ within 10% of that figure
def DisplayHighestEmployees(numEmployees_array):
    pass

#main program
"""
