output_1 = "She says 'How are u?' I reply 'Ok'"
print(output_1)

output_2 = 'She says "How are u?" I reply "Ok"'
print(output_2)

#the result is red line is didn't have \ between the alphabet and symbol
output_3 = 'She says "How\'re are u?" I reply "Ok"'
print(output_3)

output_4 = ("The monster looked at me."
            "I looked back at the monster."
            "We smiled at each other."
            )
print(output_4)

# with double quote in front "" "....." ""  , it will allow symbol and space, style print out in result
output_5 = """The monster looked at me."
            "I looked back at the monster."
            "We smiled at each other."""
print(output_5)

#remind the quote, output is different
a = "Apple"
print(a)  # result >>> Apple
print("a") #result >>> a