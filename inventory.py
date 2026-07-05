# import library
from tabulate import tabulate


# define a class 'shoe'
class Shoe():
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}," 
        f"{self.quantity}")


# create an empty list to store shoe objects
shoes_list = []


# define a function that reads data from a text file, uses it to create shoe objects,
# and adds it to the empty list
def read_shoes_data():
    
        try:
            with open ("inventory.txt", "r+") as file:
                for line in file.readlines()[1:]:
                    words = line.replace("\n", "").split(",")

                    country = words[0]
                    code = words[1]
                    product = words[2]
                    cost = float(words[3])
                    quantity = int(words[4])

                    shoe_inventory = Shoe(country, code, product, cost, 
                                          quantity)
                    
                    shoes_list.append(shoe_inventory)                        

        except FileNotFoundError:
            print("The file that you are trying to open does not exist")

# run the function
read_shoes_data()


# define a function that allows users to create a new shoe object and add it to the list
def capture_shoes():

    country = input("\nWhat country is the shoe from?")
    code = input("\nWhat is the shoe's code?")
    product = input("\nWhat is the product name?")
    cost = float(input("\nWhat is the cost of the shoe?"))
    quantity = int(input("\nWhat quantity of the shoe is available?"))

    user_shoe = Shoe(country, code, product, cost, quantity)

    shoes_list.append(user_shoe)

    pass


# define a function that displays the list in a table format
def view_all():

    table = []

    for shoe in shoes_list:

        country = shoe.country
        code = shoe.code
        product = shoe.product
        cost = shoe.cost
        quantity = shoe.quantity

        row = [country, code, product, cost, quantity]

        table.append(row)

    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", 
                                   "Quantity"], tablefmt="fancy_grid"))

    pass


# define a function that finds the shoe with the lowest quantity and asks the user
# whether they would like to restock it
def re_stock():

    lowest_shoe = shoes_list[0]

    for shoe in shoes_list:

        if shoe.quantity < lowest_shoe.quantity:
            lowest_shoe = shoe    


    print(f"\nThe shoe with the lowest quantity is {lowest_shoe.product} with " 
    f"{lowest_shoe.quantity} left in stock.")
    print()
    print("Would you like to restock?")
    option = input("\n1. Yes \n2. No")
    
    if option == "Yes" or option == "yes" or option == "1":

        number = int(input("\nHow many extra stock would you like to add on?"))

        lowest_shoe.quantity += number

        with open ("inventory.txt", "w") as file:

            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoes_list:

                lines = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},"
                f"{shoe.quantity}\n"

                file.write(lines)

    
    elif option == "No" or option == "no" or option == "2":
        pass

    else:
        print("\nInput not recognised.")

    pass



# define a function that will search for a shoe in the list using it's code
def search_shoe():

    target = input("\nPlease type a shoe code:")

    for shoe in shoes_list:

        if target == shoe.code:
            print(f"\nShoe {target} is a {shoe.product} from {shoe.country}")

            return

    print("\nCode not recognised. Please try again.")
    
    pass


# define a function that calculates the total value for each shoe
def value_per_item():

    print("\nValues of our Shoes:")

    for shoe in shoes_list:

        value = shoe.quantity * shoe.cost

        print()
        print(f"{shoe.product} -> £{value}")

    pass


# define a function that determines the product with the highest quantity and
# prints it as being for sale
def highest_qty():

    highest_shoe = shoes_list[0]

    for shoe in shoes_list:

        if shoe.quantity > highest_shoe.quantity:
            highest_shoe = shoe


    print(f"\nBuy the {highest_shoe.product} now for only £{highest_shoe.cost}!")

    pass


# create a menu inside a while loop that allows users to select which function they
# would like to continue with
while True:

    print()
    print("Welcome to the inventory menu. Pick an option:")
    print()
    choice = input("""
    1. View our inventory 
    2. Add to the inventory 
    3. Restock inventory 
    4. Search the inventory 
    5. Show value per inventory item 
    6. Recommend an item to purchase
    
    (please input a number)""")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    else:
        print("Choice not recognised. Please try again.")
                   

    

    

    










    




