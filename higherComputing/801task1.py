from dataclasses import dataclass

@dataclass
class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

BMIrecord = [person() for index in range(5)]

# this in input validation, but N5 level so don't worry about it in exams
thisHeight = float(input("Please enter your height: "))
while thisHeight <= 0 or thisHeight > 2.5:
  print("ERROR! YOUR ARE TOO BIG / SMALL")
  thisHeight = float(input("Please enter your height: "))


BMIrecord[1].height = 1.75
BMIrecord[1].weight = 70.5
BMIrecord[1].bmi = BMIrecord[1].weight / (BMIrecord[1].height **2 )

BMIrecord[1].height = 1.62
BMIrecord[1].weight = 55.8
BMIrecord[1].bmi = BMIrecord[1].weight /( BMIrecord[1].height **2 )

BMIrecord[1].height = 1.88
BMIrecord[1].weight = 95.2
BMIrecord[1].bmi = BMIrecord[1].weight / (BMIrecord[1].height **2 )

BMIrecord[1].height = 1.70
BMIrecord[1].weight = 82.3
BMIrecord[1].bmi = BMIrecord[1].weight / (BMIrecord[1].height **2 )

BMIrecord[1].height = 1.80
BMIrecord[1].weight = 68.0
BMIrecord[1].bmi = BMIrecord[1].weight / (BMIrecord[1].height **2 )

print(BMIrecord[0])
print(BMIrecord[1])
print(BMIrecord[2])
print(BMIrecord[3])
print(BMIrecord[4])