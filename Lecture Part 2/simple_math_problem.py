#A teacher has 3456 sweet to distribute
#to 127 students
#how many sweets does each student get?
#how many are left over?
#

num_sweets = 3456
student = 127



#A teacher has 3,123,456 sweet to distribute
#to 127 students
#how many sweets does each student get?
#how many are left over?
#

sweets = 3_123_456
num_students = 127

num_students_per_students = sweets // num_students
remaining_sweets = sweets % num_students

print(f"Each student will get {num_students_per_students} sweets.")
print(f"There are {remaining_sweets} sweets left")
