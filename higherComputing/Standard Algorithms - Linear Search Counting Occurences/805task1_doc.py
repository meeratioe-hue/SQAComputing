

OwnsAnIPhone =["yes", "no", "no", "no", "yes","yes","yes","yes"]
counter = 0

for i in range(len(OwnsAnIPhone)):
    if OwnsAnIPhone[i] == "yes":
         counter = counter + 1
    else:
         counter = counter

print (counter, "owns Iphones")

#i is index. index is to go along 
#len is the length of the array