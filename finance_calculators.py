# Investment & Home loan calculator

import math

# Statrting statments
print("\n------------------------------------------------------------------------------------")
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond       - to calculate the amount you will have to pay on a home loan")
print("------------------------------------------------------------------------------------\n")


# User input
choice_1 = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Validations of the user input
if choice_1 == "investment" or choice_1 == "bond":
    print()
else:
    print("You have not entered an appropriate choice. Plese enter 'investment' or 'bond'. ")

# Investment calculation
# 1st user inputs, 2nd calculations and validation, 3rd displaying the final amount
if choice_1 == "investment":
    amount = float(input("How much money will you be investing with us? "))
    percentage = float(input("What is your interest rate? "))
    time = float(input("How many years do you wish for your money to be invested with us? "))
    interest = input("Would you like 'simple' or 'compound' interest? ").lower()
    
    if interest == "simple":
        final_amount = amount * (1 + ((percentage/100) * time))
    elif interest == "compound":
        final_amount = amount * math.pow((1 + (percentage/100)), time)
    else:
        print("You have not entered an appropriate choice. Plese enter 'simple' or 'compound'. ")

    final_amount_r = round(final_amount,2)
    print(f"Your initial investment should be turned into {final_amount_r}.")

# Bond calculation
# 1st user inputs, 2nd calculation, 3rd displaying monthly payments
if choice_1 == "bond":
    house_value = float(input("How much is the house worth? "))
    interest = float(input("What is your interest rate? "))
    months = float(input("How many months do you wish to take to repay the loan? "))
    
    repayment = (((interest/100) / 12) * house_value) / (1 - (1 + ((interest/100)/12)) ** (-months))
    repayment_r = round(repayment,2)

    print(f"Your monthly payment would be {repayment_r}.")
