from dataclasses import dataclass
@dataclass
class student():
    studentID : int = ""
    email : str = ""
    password : str = ""
    yearGroup : int = 10

theStudents = [student() for i in range(10)] 

def writeAllStudentsToFile (theStudents):
    with open("student.txt", "w") as writefile:
        for i in range(10):
            writefile.write(str(theStudents[i].studentID) + "," + theStudents[i].email + "," + theStudents[i].password + "," + str(theStudents[i].yearGroup) + "\n")


writeAllStudentsToFile(theStudents)


