#syntax error:
#is an error in spelling/grammer when coding
PetPurchased = ["Dog", "Dog", "Cat", "Rabbit", "Hamster", "Cat", "Hamster", "Budgie"]

LastUser = 0
TargetAnimal = "Dog"
for i in range(len(PetPurchased)):
    if TargetAnimal == PetPurchased[i]:
       LastUser = i + 1
print(TargetAnimal, "was found in position:", LastUsers)

