import statistics
from statistics import median

# ask the user to imput 10 floats and store them in a list

number_list = []

for i in range(1, 11):
    number = float(input("Please enter a number:"))
    number_list.append(number)

sum = sum(number_list)

print(f"The sum of your numbers is {sum}")

print(f"The index of the minimum number is {number_list.index(min(number_list))}")

print(f"The index of the maximum number is {number_list.index(max(number_list))}")

print(f"The average of your numbers is {round(sum/10, 2)}")

print(f"The median of your numbers is {median(number_list)}")



