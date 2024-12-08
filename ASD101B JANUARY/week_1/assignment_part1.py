# Write a function named "calculate_bmi" that takes two required parameters: "height" (in meters as float) and "weight" (in kilograms as float). The function should calculate the BMI using the formula: BMI = weight / (height * height) and return the calculated BMI as a float.

# The function should also print a message based on the calculated BMI as follows:

# If BMI is less than 16, print: "Your BMI is {bmi:.2f}. You are severely underweight."
# If BMI is between 16 and 16.9, print: "Your BMI is {bmi:.2f}. You are underweight."
# If BMI is between 17 and 18.4, print: "Your BMI is {bmi:.2f}. You are mildy underweight."
# If BMI is between 18.5 and 24.9, print: "Your BMI is {bmi:.2f}. You have a normal weight."
# If BMI is between 25 and 29.9, print: "Your BMI is {bmi:.2f}. You are overweight."
# If BMI is between 30 and 34.9, print: "Your BMI is {bmi:.2f}. You are obese class 1 (Moderate)."
# If BMI is between 35 and 39.9, print: "Your BMI is {bmi:.2f}. You are obese class 2 (Severe)."
# If BMI is 40 or greater, print: "Your BMI is {bmi:.2f}. You are obese class 3 (Very severe or morbidly obese)."


# Example usage of the "calculate_bmi" function:
# height = 1.75
# weight = 65.5

# bmi = calculate_bmi(height, weight)

def pounds_to_kilograms(pounds):
    return 0.45359237 * pounds
def feet_and_inches_to_meters(feet, inches):
    total_feet = feet + inches/12
    return 0.3048 * total_feet

def calculate_bmi (height, weight):
    bmi = weight  / height ** 2
    message = f"Your BMI is {bmi:.2f}. "
    if bmi < 16:
        print(message + " You are severely underweight.")
    elif bmi <= 16.9:
        print(message + "You are underweight. ")
    elif bmi <= 18.4:
        print(message + "You are mildly underweight. ")
    elif bmi <= 24.9:
        print(message + "You have a normal weight. ")
    elif bmi <= 29.9:
        print(message + "You are overweight. ")
    elif bmi <= 34.9:
        print(message + "You are obese class 1 (Moderate). ")
    elif bmi <= 39.9: 
        print(message + "You are obese class 2 (Severe)")
    else:
        print(message + "You are obese class 3 (Very Severe or Morbidly Obese). ")
        return bmi
    
    height = feet_and_inches_to_meters(5, 7)
    weight = pounds_to_kilograms(190)

    bmi = calculate_bmi(height, weight)





