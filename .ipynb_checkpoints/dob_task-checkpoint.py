names = []
bdays = []

with open ("DOB.txt", "r+") as file:
  for line in file:
      words = line.split()
      
      if len(words) > 0:        

          names.append(" ".join(words[:-3]))
          bdays.append(" ".join(words[-3:]))

list_names = "\n".join(names)
list_bdays = "\n".join(bdays)

print(f"Names: \n{list_names}\n")
print(f"Birthdays: \n{list_bdays}\n")
          

