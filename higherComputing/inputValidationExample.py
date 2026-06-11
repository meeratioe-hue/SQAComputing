# this in input validation, but N5 level so don't worry about it in exams
thisHeight = float(input("Please enter your height: "))
while thisHeight <= 0 or thisHeight > 2.5:
  print("ERROR! YOUR ARE TOO BIG / SMALL")
  thisHeight = float(input("Please enter your height: "))