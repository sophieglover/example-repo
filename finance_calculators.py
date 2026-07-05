import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# ask the user to choose which calculation they want to do
calc_choice = input('Enter either "investment" or "bond" from the menu above to proceed:')

# investment choice
if (calc_choice == "Investment") or (calc_choice == "investment") or (calc_choice == "INVESTMENT"):

    # ask how much money the user is depositing
    deposit = float(input("How much money are you depositing?"))

    # ask the user their interest rate
    interest_rate = float(input("What is your interest rate (as a percentage)?"))

    # ask the user how long they plan to invest
    years_investing = float(input("How many years do you plan to invest?"))

    # ask whether the user wants 'simple' or 'compound' interest
    interest = input("Would you like simple or compound interest?")

    # simple interest choice
    if (interest == "Simple") or (interest == "simple") or (interest == "SIMPLE"):

        #calculating the amount after adding interest
        total_amount = deposit * (1 + (interest_rate/100) * years_investing)
            
        print(f"The amount you'll have after applying interest is £{round(total_amount,2)}.")

    # compound interest choice
    elif (interest == "Compound") or (interest == "compound") or (interest == "COMPOUND"):

        #calculating the amount after adding interest
        total_amount = deposit * math.pow((1+(interest_rate/100)), years_investing)

        print(f"The amount you'll have after applying interest is £{round(total_amount,2)}.")

    # display an error message if choice not recognised        
    else:
        print("Error: choice not recognised.")

                
# bond choice
elif (calc_choice == "Bond") or (calc_choice == "bond") or (calc_choice == "BOND"):

    # ask the user the present value of the house
    present_value = float(input("What is the present value of the house?"))

    # ask the user the interest rate
    interest_rate = float(input("What is the interest rate?"))

    # ask the user the number of months they plan to take to repay the bond
    months = float(input("How many months do you plan to take to repay the bond?"))

    # calculate the amount the user will have to repay on a home loan each month
    repayment = (((interest_rate/100)/12)*present_value)/(1-(1+((interest_rate/100)/12))**(-1 * months))

    print(f"The amount of money you will have to repay each month is £{round(repayment, 2)}.")
                

# error message if choice not recognised
else:
    print("Error: choice not recognised.")





