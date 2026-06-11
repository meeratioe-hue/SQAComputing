PetPurchased = ["Dog", "Dog", "Cat", "Rabbit", "Hamster", "Cat", "Hamster", "Budgie"]
AllUsers = []
PositionOfUser = 0
TargetAnimal = "Hamster"


for i in range (len(PetPurchased)):
    if PetPurchased[i] == TargetAnimal:
        print ("position:", PositionOfUser)
    PositionOfUser += 1
