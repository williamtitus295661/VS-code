# 2. Calories BurnedRunning on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

calories_per_minute = 4.2

for minutes in range(10, 35, 5):
    calories = minutes * calories_per_minute
    print(f"Minutes:{minutes} Calories Burned:{calories}")
    