calc_list = []

while True:
    print("1. Perform a calculation")
    print("2. Print previous calculations")

    choice = input("Please select 1 or 2:")

    if choice == "1":

        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        operation = input("Pick an operation: +, -, x, or ÷:")

        if operation == "+":
            ans = num1 + num2
            calc = (f"{num1} + {num2} = {ans}")
            calc_list.append(calc)
            print(calc)
            with open("equations.txt", "a") as f:
                f.write(calc + "\n")
            

        elif operation == "-":
            ans = num1 - num2
            calc = (f"{num1} - {num2} = {ans}")
            calc_list.append(calc)
            print(calc)
            with open("equations.txt", "a") as f:
                f.write(calc + "\n")
            

        elif operation == "x":
            ans = num1 * num2
            calc = (f"{num1} x {num2} = {ans}")
            calc_list.append(calc)
            print(calc)
            with open("equations.txt", "a") as f:
                f.write(calc + "\n")
            

        elif operation == "÷":
            if num2 == 0:
                raise Exception(f'num value ({num2}) is equal to 0')
            else:
                ans = num1 / num2
                calc = (f"{num1} ÷ {num2} = {ans}")     
                calc_list.append(calc)
                print(calc)
                with open("equations.txt", "a") as f:
                    f.write(calc + "\n")

        else:
            print("Error: choice not recognised. Please try again.")


    elif choice == "2":

        file = None

        try:
            file = open('equations.txt', 'r')

            saved_calcs = file.read()
            print(saved_calcs)

        except FileNotFoundError:
            print("The file that you are trying to open does not exist")

        finally:
            if file is not None:
                file.close()







        
