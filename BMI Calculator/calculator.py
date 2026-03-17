# This is to simplify and compartmentalize all of my calculations for testing
# ...and because I like how it looks better.
    

# height to meters & lbs to kg conversions
def conversions(heightFT, heightIN, weight):
    heightIN = heightIN + (heightFT * 12)
    kilos = weight * 0.45
    meters = heightIN * 0.025
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


