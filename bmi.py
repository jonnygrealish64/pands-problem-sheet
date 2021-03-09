# bmi.py
# This program will calculate the user's Body Mass Index
# Author: Jonathon Grealish

# The variable height will store the user's height input as a float with decimals.
# The variable weight will store the user's weight input as an integer. 

height = float(input("Enter your height (in m): "))
weight = int(input("Enter your weight (in kg): "))

print ("Your calculated BMI is: ", round(weight / height**2,2))
# The formula to calculate BMI is as follows:
# BMI = Weight/Height^2; **2 will calculate height to the power of 2.
# Round will round the result to two decimal places, indicated by the second 2 in the formula.