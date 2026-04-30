scores = [55, 66, 77, 43, 89, 98, 65, 73, 25, 82, 85]

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

print(f"Range: {lowest} - {highest}")
print(f"Average: {average:.1f}")

print("=== Other Case ===")
scores_1 = scores
scores_1[0] = 83   #modify scores_1
#result was same because both point to the same list
print(scores_1)
print(scores)


print()
print("=== Fixed the 2 variable not same result ===")
scores_2 = scores[:]   #using slicing to make a copy
scores_2[-1] = 100
#result not same
print(scores_2)
print(scores)

print()
print("Other way")
scores_3 = [] + scores
scores_3[0] = "Teh"
print(scores_3)
print(scores)
