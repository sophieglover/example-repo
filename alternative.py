string = input("Enter a sentence:")

string_split = string.split()

for i in range(len(string_split)):
    if i % 2 == 0:
        string_split[i] = string_split[i].lower()
    else:
        string_split[i] = string_split[i].upper()

print(" ".join(string_split)) 

string_list = list(string) 

for i in range(len(string_list)):
    if i % 2 == 0:
        string_list[i] = string_list[i].lower()
    else:
        string_list[i] = string_list[i].upper()

print("".join(string_list)) 