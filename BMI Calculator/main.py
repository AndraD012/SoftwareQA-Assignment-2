# sources cited here: GeeksForGeeks used for any python questions/refresher help
import time

print("Welcome to your Personal BMI Calculator!")
print("\nAll I need to begin is your height in feet and inches and your weight in pounds.")
print("Note: Please use only numbers for your input, not any words. (i.e. 5, 10, 128)")

# This is to simplify and compartmentalize all of my calculations for testing
# ...and because I like how it looks better.
    

# height to meters & lbs to kg conversions
def conversions(heightFT, heightIN, weight):
    heightIN = heightIN + (heightFT * 12)
    meters = heightIN * 0.025
    kilos = weight * 0.45
    return meters, kilos

# get the BMI
def bmiCalc(meters, kilos):
    bmi = kilos / (meters * meters)
    return bmi

# now to sort!
def sort(bmi):
    if bmi < 18.5:
        bmiSort = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmiSort = "Normal Weight"
    elif bmi >= 25 and bmi <= 29.9:
        bmiSort = "Overweight"
    elif bmi >= 30:
        bmiSort = "Obese"
    
    return bmiSort

# verification 1
while True:
    try:
        feet = float(input("\nPlease input the amount of feet in your height: "))
        break
    except ValueError:
        print("\nInvalid input! Please enter a number, nothing else!")

# verification 2
while True:
    try:
        inches = float(input("\nPlease input the inches portion of your height: "))
        break
    except ValueError:
        print("\nInvalid input! Please enter a number, nothing else!")

# verification 3
while True:
    try:
        weight = float(input("\nLastly, input your weight in pounds here: "))
        break
    except ValueError:
        print("\nInvalid input! Please enter a number, nothing else!")


# verify(feet, inches, weight)
print("\n\n ...Now give me just a moment...\n\n")
# wait for 2 seconds just for funsies
time.sleep(2)

# convert height to meters
meters, kg = conversions(feet, inches, weight)

# calculate bmi from those
bmi = bmiCalc(meters, kg)

#turn bmi into a string bc apparently its a problem I'm tired.
stringBMI = str(bmi)

answer = sort(bmi)

print("Finally, your BMI is " + stringBMI + " and you are classified as " + answer)
print("Have a nice day!")

