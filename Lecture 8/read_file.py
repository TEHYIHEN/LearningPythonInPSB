file_in = open('quotes.txt','r')
print("Current position: ",file_in.tell())
first_3_chars = file_in.read(3)
print("First 3 chars:" ,first_3_chars)
print("Current position after reading: ",file_in.tell())

rest_of_line = file_in.readline()
print("Rest of line:", rest_of_line)

second_line = file_in.readline()
print("Second line:", second_line)

print()
print("*"*20)
rest_of_passage = file_in.read()
print("Rest of line:", rest_of_passage)
print("Current position after reading: ",file_in.tell())

print()
print("="*20)
more_text = file_in.read(100)
print(f"More text: [{more_text}]")

print()
print("-"*20)
file_in.seek(0)  #go back to start
all_lines = file_in.readlines()  #give list of all line , example ['Hello World\n', 'My name is Teh\n', 'I love eat durian\n', 'Damn Cat\n', 'I hate cat\n', 'I love puppy\n', '2']
print(f"All lines: {all_lines}")
print()
for i in range(len(all_lines)):
    print(f"{i:2} {all_lines[i]}")



file_in.close()