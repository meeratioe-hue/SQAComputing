PetPurchased = ["Dog", "Dog", "Cat", "Rabbit", "Hamster", "Cat", "Hamster", "Budgie"]
AllUsers = []
PositionOfUser = 0
TargetAnimal = "Hamster"
PosFound = 0


for i in range (len(PetPurchased)):
    if PetPurchased[i] == TargetAnimal:
        print ("position:", PositionOfUser)
        posFound = i
    PositionOfUser += 1

print(posFound)

   



