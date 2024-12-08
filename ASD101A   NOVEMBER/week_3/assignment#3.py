# 7. Write an if-else statement that determines whether the points variable is outside the range of 9 to 51. If the variable’s value is outside this range it should display “Invalid points.” Otherwise, it should display “Valid points.”
points = int(input(" enter a number of points"))
if points < 9 or points > 51:
    print(" Invalid points!")
else:
    print("Valid points!")
#     And  the following Chapter 3 checkpoint activities. For coding question include your code snippets and output.

# 3.6 Write an if statement that assigns 0 to x if y is equal to 20.
y = int(input("Pick a value for y."))
if y == 20:
    x = 0
    # 3.7 Write an if statement that assigns 0.2 to commissionRate if sales is greater than or equal to 10000.
    sales = float(input("Pick a value for sales: $"))
    if sales >= 10000:
        commisionRate = 0.2
    # 3.15 The following truth table shows various combinations of the values true and false connected by a logical operator.

# Complete the table by circling T or F to indicate whether the result of such a combination is true or false.

# Logical Expression    Result (circle T or F)
# True and False    T    (F)
# True and True    (T)    F
# False and True    T    (F)
# False and False    T    (F)
# True or False    (T)    F

# 3.16 Assume the variables a = 2, b = 4, and c = 6.

# Circle T or F for each of the following conditions to indicate whether its value is true or false.

# a == 4 or b > 2    (T)    F
# 6 <= c and a > 3    T    (F)
# 1 != b and c != 3    (T)    F
# a >= −1 or a <= b    (T)    F
# not (a > 2)    (T)   F


# 3.18 Write an if statement that displays the message “The number is valid” if the value referenced by speed is within the range 0 through 200.

speed = float(input("Pick a value for speed: "))
if speed >= 0 and speed <= 200:
    print("The number valid")


# 3.19 Write an if statement that displays the message “The number is not valid” if the value referenced by speed is outside the range 0 through 200.
if speed < 0 or speed > 200:
    print("The number is not valid! ")


 


