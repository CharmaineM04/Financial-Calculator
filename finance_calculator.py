# Task 11 - Capstone Project 1
# Writing a program for a small financial company to access two financial calculators.
# This will include an investment calculator and a home loan repayment calculator.

# Import libraries
import math

# Get user input for choice of calculator i.e. investment or bond.
finance_type = input(""" 
Investment - to calculate the anount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on home loan

Enter either 'investment' or 'bond' from the manu above to  proceed :

                    """).lower()

# Calculate and display investment returns
# Get user input on the amount, rate, years and interest type to enter into invest
if finance_type == "investment" :
      deposit_amount = float(input("Enter the amount you are going  to deposit : "))
      interest_rate = float(input("Enter the interest as a percentage : "))
      term_of_investment = float(input("Enter the number of years you plan on investing : "))
      type_of_interest = input("Enter 'simple' or 'compound' interest : ").lower() 

# Creating indented conditional statement to display the results based on user's choice of interest type.
# Entering formulas for simple and compound interest depending on user choice.     
      if type_of_interest == "simple" : 
            amount = deposit_amount*(1+(interest_rate/100)*term_of_investment)
            print("Your return will be R{} after {} years of investment at {}% interest rate".format(amount,term_of_investment,interest_rate))
      elif type_of_interest == "compound" :
           amount = deposit_amount*math.pow((1+interest_rate/100),term_of_investment)
           print("Your return will be R{} after {} years of investment at {}% interest rate".format(amount,term_of_investment,interest_rate))
      else:
           print("invalid entry, enter 'simpe'or 'compound' to continue")

# Bond repayment calculations.
# Getting input from user on house value, interest rate and number of months taken to pay bond, to enter into bond calculator.
elif finance_type == "bond" :
     house_value = float(input("Enter the present value of the house : "))
     bond_interest = float(input("Enter the interest rate in percentage : "))
     term_in_month = int(input("Enter the number of months you plan to repay the bond : "))
     monthly_interest_rate = (bond_interest/100)/12
     bond_repayment = (monthly_interest_rate*house_value)/(1-(1+monthly_interest_rate)**(-term_in_month))
     print("Your monthly bond repayment is R{} per month at {}% interest rate".format(bond_repayment,bond_interest))
else:
  print("Invalid entry, chose the correct type of finance to continue")   
