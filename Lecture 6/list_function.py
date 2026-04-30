animals_1 = ["elephant", "crocodile", "hippopotamine"]
animals_2 = ["hyena", "cheetah", "honey badger"]

animals_4 = animals_1 + animals_2
print(animals_4)

animals_3 = [] + animals_4  #create a new list with animals_4

print()
print(f"Number of animals: {len(animals_3)}")

print("Insert")
animals_3.insert(0, "tiger")
print(animals_3)

print("Append")
animals_3.append("emu")
print(animals_3)

print("Pop[4]")
animals_3.pop(4)  #remove hyena
print(animals_3)

print("Pop()")
animals_3.pop()  #remove emu, the last
print(animals_3)

print("Remove")
animals_3.remove("elephant")
print(animals_3)


print("Sort")
animals_3.sort()  # sort by ascending order(abc)
print(animals_3)

print("Reverse Sort")
animals_3.sort(reverse=True)  #sort by descending
print(animals_3)

print("Append 2")
animals_3.append("warthog")
animals_3.append("baboon")
print(animals_3)

print("Reverse")
animals_3.reverse()
print(animals_3)

print("Sorted")
ascending_animals = sorted(animals_3)
descending_animals = sorted(animals_3, reverse=True)

print(ascending_animals)
print(descending_animals)

print("Latest Status")
print(animals_3)
print(animals_4)