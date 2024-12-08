# Write your own function, named Quizzer, which when called will do the following:

# Generate 2 random integers between 1-10 (inclusive)
# Print the 2 numbers to the screen as a math problem, e.g. 2 * 10 = ?
# Ask the user what the product (multiplication) of the 2 numbers is (e.g. the answer to the math problem)
# Return True if the user's answer was correct, False otherwise.
# Additionally, your solution should include a main program which, when your python file is run will call your Quizzer function (one time) and store the result from Quizzer in a new variable named success. If success is True after Quizzer is done running, print to the screen: "Good job!" Else, print to the screen the "Better luck next time."

import random
def Quizzer():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    product = a * b
    print(f"{a} * {b} = ?")
    answer = int(input("What is the product? "))
    return product == answer
def main():
    success = Quizzer()
    if success:
        print("Good job!")
    else:
        print("Better luck next time!")
        main()




