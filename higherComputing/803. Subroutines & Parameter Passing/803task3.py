#this is a procedure because it returns 0 parameters
def module1(first, second, third):
  volume = first * second * third
  print("Volume =",volume)

#this is a function because it returns 1 value
def module2(monday):
  monday = monday/10
  return monday

#this is a function because it returns 1 value
def module3(blue, red):
  total = 0
  for counter in range(blue, red):
    total = total + 2
    print(total)
    return total

#this is a function because it returns 1 value 
# the % symbol means remainder. ex: 4%3 = 1
def module4(up, down):
  middle = up % down
  top = int(up/down)
  total = middle + top
  return total

