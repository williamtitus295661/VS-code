# 2) Write a while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If so, the loop should repeat, otherwise it should terminate

keep_going = True
while keep_going:
    number1 = int(input("Enter a number for the first value.   "))
    number2 =int(input("Enter a number for the second value.   "))
    print(f"{number1}  + {number2}  = {number1 + number2}")
    answer = input("keep going? (yes/no):")
    while answer not in {'yes', 'no'}:
        print("You must answer yes or no.")
        answer = input(" Keep going? (yes/no):")
        keep_going = answer == "yes"



# 4) Write a loop that asks the user to enter a number. The loop should iterate 10 times and keep a running total of the numbers entered.

total = 0
for i in range(10):
    number = int(input("Choose number.  "))
    total += number
    print(total)





# Chapter 4  Checkpoint Activities:

# 4.6 How many times will 'Hello World' be printed in the following program? Explain the output.

#   count = 10
#    while count < 1:
#          print('Hello World')
# 0, because the condition initially evaluates to False

 

# 4.9 What will the following code display?

#  for number in range(6):
#      print(number)

# 0, 1, 2, 3, 4, 5


# 4.10 What will the following code display?

#  for number in range(2, 6):
#      print(number)

# 2, 3, 4, 5

 

# 4.17 Rewrite the following statements using augmented assignment operators:

# quantity = quantity + 1
# quantity += 1

# days_left = days_left − 5
# quantity -= 5

# price = price * 10
# price += 10

# price = price / 2
# price /= 2 


 