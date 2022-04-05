# Exercise 1 - BMI 2.0
# 
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# 
# It should tell them the interpretation of their BMI based on the BMI value.
# 
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# 
# Warning you should round the result to the nearest whole number. 
# The interpretation message needs to include the words in bold from 
# the interpretations above. e.g. underweight, normal weight, overweight, 
# obese, clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))
strMessage = f"Your BMI is {bmi}"
if (bmi > 35):
    print(strMessage + ", you are clinically obese.")
elif (bmi <= 35 and bmi > 30):
    print(strMessage + ", you are obese.")
elif (bmi <= 30 and bmi > 25):
    print(strMessage + ", you are slightly overweight.")
elif (bmi <= 25 and bmi > 20):
    print(strMessage + ", you have a normal weight.")
else:
    print(strMessage + ", you are underweight.")
