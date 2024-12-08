# 1. Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z if the variable x is greater than 100.
x = int(input("Pick a value for x: "))
if x > 100:
    y = 20
    z = 40
    # 2. Write an if statement that assigns 0 to the variable b, and assigns 1 to the variable c if the variable a is less than 10.
    a = int(input("pick a value for a:"))
    if a < 10:
        b = 0
        c = 1
    #    3. Write an if-else statement that assigns 0 to the variable b if the variable a is less than 10. Otherwise, it should assign 99 to the variable b.
    if a < 10:
        b = 0
    else: b = 99
#     4. The following code contains several nested if-else statements. Unfortunately, it was written without proper alignment and indentation. Rewrite the code and use the proper conventions of alignment and indentation.
score = int(input(" what is your score 0-100"))
A_score = 90
B_score = 80
C_score = 70
D_score = 60

if score >= A_score:
        print('Your grade is A,')
elif score >= B_score:
            print('Your grade is B.')
elif score >= C_score:
         print('Your grade is C.')
elif score >= D_score:
         print('Your grade is D.')
else:
         print('Your grade is F.')
        #  5. Write nested decision structures that perform the following: If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2.
         amount1 = int(input("pick a value for amount 1"))
         amount2 = int(input("pick a value for amount 2"))
         if amount1 > 10 and amount2 < 100:
                if amount1 >= amount2:
                       print(amount1)
                else:
                        print(amount2)
                    # 6. Write an if-else statement that displays 'Speed is normal' if the speed variable is within the range of 24 to 56. If the speed variable’s value is outside this range, display 'Speed is abnormal'.
                speed = int(input("how fast were you going?"))
                if speed >= 24 and speed <=56:
                       print("speed is normal")
                else:
                       print("speed is abnormal.")
                       
                






                    
   