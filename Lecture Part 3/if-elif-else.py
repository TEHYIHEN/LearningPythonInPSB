score = float(input("Enter your score: "))

if 80 <= score <= 100:
    grade = "A"
elif 60 <= score < 80:
    grade = "B"
elif 50 <= score < 60:
    grade = "C"
elif 0 <= score < 50:
    grade = "D"
else:
    grade = "NA"

if grade != "NA":
    print(f"Your grade is {grade} for score {score:.0f}.")
else:
    print("Please enter a valid score (0 - 100).")