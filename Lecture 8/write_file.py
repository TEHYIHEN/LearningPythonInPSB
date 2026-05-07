file_out = open("quotes.txt","w")
#reading only ('r'), writing ('w'), and appending ('a')

file_out.write("Hello World\n"
               "My name is Teh\n"
               "I love eat durian\n"
               )

file_out.write("Damn Cat\n"
               "I hate cat\n"
               "I love puppy\n"
               )
number = 2
file_out.write(f"{number}")


file_out.close()