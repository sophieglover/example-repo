i = 0
sum = 0

while True:
    number = int(input("Please enter a number:"))
    
    if number == 0:
        print("Invalid number")
        continue
        
    if number == -1:
        break

    i += 1
    sum += number
    
if i>0:
    average = sum / i
    print(f"The average of your valid numbers is {average}") 

else:
    print("No valid numbers were entered")
