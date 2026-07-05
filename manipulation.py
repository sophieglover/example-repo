str_manip = input("Enter a sentence:")

print(f"The length of your sentence is {len(str_manip)} characters")

# find the last letter in the sentence and replace every occurence of this letter with @

print(str_manip.replace(str_manip[-1], '@'))

# print the last three characters in the sentence backwards

print(str_manip[-1:-4:-1])

# create a five letter word that is made up of the first three characters and the last two characters in the sentence

first_three = str_manip[:3]
last_two = str_manip[-2:] 

print(first_three + last_two)