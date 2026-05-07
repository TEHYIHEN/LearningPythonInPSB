phrase = "The fish quote: Give a man a fish and you feed him for a day;"

sub_text = "fish"

num_instances = phrase.count("fish")
print(f"There are {num_instances} instances of （fish）")

index = phrase.find("fish")
print(index)

# find all here
print()
print(f"------ Finding all indexes of {sub_text} ----------")
count = 0
current_index = 0
while count < num_instances:
    index = phrase.find(sub_text, current_index)
    if index != -1:  # if found
        print(f"{sub_text} found at index {index}") # print position
    current_index = index + 1  # update new position to start locating fish
    count += 1  # update the number of fish found



print()
print("="*20)
print()

array = ["Apple","Banana","Cat","Apple","Dog"]

find_apple = "Apple"

num_count = array.count(find_apple)
print(f"There are {num_count} instances of {find_apple}")

num_index = array.index(find_apple)
print(f"Index of is {num_index}")

print(array.index(find_apple, 1))

