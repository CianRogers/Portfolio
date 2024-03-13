import math 
print("investment - to calculate the amount of interest you'll earn on your investment ")
print("bond - to calculate the amount of you'll have to pay on a home loan ")
investment_bond_investment = input("Enter either 'investment' or 'bond' from the menu above to proceed ")
# remove casesensitity using .casefold so Investment, INVESTMENT OR investment can be entered
if investment_bond_investment.casefold() == "investment":
    print("Entering investment menu")
elif investment_bond_investment.casefold() == "bond":
# remove casesensitity using .casefold so Bond, BOND OR bond can be entered
    print("Entering bond menu")
# if anything other than bond or invvestment entered show an eror message
else:
    print("Error! Please enter 'investment' or 'bond'")
if investment_bond_investment.casefold() == "investment":
# if investment entered ask for deposit ammount, interest rate and years of investing
    deposit_ammount = int(input("How much are you depositing "))
    interest_rate = int(input("Please enter your interest rate "))
    years_of_investing = int(input("Please enter how many years you want to invest for "))
    interest = (input("Would you like to calculate simple or compound interest? Please enter simple or compound "))
    divided_interest = interest_rate / 100
    if interest.casefold() == "simple":
# if investment entered ask whether the user wants to calculate simple ot compound interest
# if the user wants simple calculate simple interest of inputted values
        simple_interest = deposit_ammount * (1 + divided_interest * years_of_investing)
        print("Your total equals", simple_interest) 
    elif interest.casefold() == "compound":
# if the user wants to calculate compound calculate compound interest of inputted values
        compound_interest = deposit_ammount * math.pow((1+divided_interest),years_of_investing)
        print("Your total equals", compound_interest)
    else:
        print("Error! please enter simple or compound")
if investment_bond_investment.casefold() == "bond":
# # if the user inputts bond calculate monthly bond repayment with inputted values
    value_house = int(input("Please enter the present value of the property "))
# Prompt the user to imput their interest rate 
    interest_rate_bond = int(input("Please enter your interest rate "))
    interest_rate_bond_divided_100 = interest_rate_bond / 100
    interest_rate_bond_divided_100_12 = interest_rate_bond_divided_100 / 12
    months_repayment = int(input("Please enter how many months you plan on taking to repay the bond "))
# Calculate the monthly repayment valvue for the user based upon their inputs
    bond_repayment = (interest_rate_bond_divided_100_12 * value_house)/(1- (1 + interest_rate_bond_divided_100_12)**(-months_repayment))
    print("The ammount you will have to repay each month is", bond_repayment) 
           
