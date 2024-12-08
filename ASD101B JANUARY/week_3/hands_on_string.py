# 2. Sum of Digits in a StringWrite a program that asks the user to enter a series of single-digit numbers with nothing separating them. The program should display the sum of all the single digit numbers in the string. For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4.

digit_str = input("Write a series of digits to be added togrther with no spaces: ")
try:
  total = 0
  for digit in digit_str:
    total += int(digit)
  print(total)
except ValueError as err:
  print(err)



