# 8. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
Sales_Tax_Rate = 0.07
Tip_Rate = .2

meal_cost = float(input(" what was the cost of the meal ? "))
sales_tax = Sales_Tax_Rate * meal_cost
tip_amount = (meal_cost + sales_tax) * Tip_Rate
total_amount = meal_cost + sales_tax + tip_amount

print(f"sales tax: ${sales_tax:.2f}")
print(f"tip: ${tip_amount:.2f}")
print(f"Total: ${total_amount:.2f}")






# 11. Male and Female Percentages 
# Write a program that asks the user for the number of males and the number of females registered in a class. The program should display the percentage of males and females in the class.Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The percentage of males can be calculated as , or 40%. The percentage of females can be calculated as , or 60%.
males = int(input("hom many males?"))
females = int (input("how many females?"))


total_students = males + females
total_females = females/total_students
total_males = males/total_students

print(f"Males:{total_males:%}")
print(f"Females:{total_females:%}")




