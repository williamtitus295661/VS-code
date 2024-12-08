# 1. Day of the WeekWrite a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if the user enters a number that is outside the range of 1 through 7.2. 
Monday = 1
Tuesday = 2
Wednsday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
day = int(input("Pick a day of the week, numbered 1 through 7, 1 for Monday , 7 for Sunday:   "))
if day == Monday:
    print("Monday") 
elif day == Tuesday:
     print("Tuesday")
elif day == Wednsday:
     print("Wednsday")
elif day == Thursday:
     print("Thursday")
elif day == Friday:
    print("Friday")
elif day == Saturday:
     print("Saturday")
elif day == Sunday:
    print("Sunday")
else:
     print("Error! Invalid input, you must enter a number between 1 and 7!  ")


# day_of_week = [
#     "Monday"
#     "Tuesday"
#     "Wednsday"
#     "Thursday"
#     "Friday"
#     "Saturday"
#     "Sunday"
#     ]
# day = int(input("Pick a day of the wee, numbered 1-7 1 for Monday and 7 for Sunday:"))
# if day >= 1 and day <= 7:
#     print(day_of_week)
# else:
#        print("Error! You have entered an invalid day, you must enter a number between 1 and 7! ")


    