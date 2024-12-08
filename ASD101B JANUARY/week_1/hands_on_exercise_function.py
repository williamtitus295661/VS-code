# Write your own function named "HappyBirthday" which takes 1 (required) integer parameter: "year", and one (required) string parameter: "name". Use the "year" input to calculate the age of the person based on the current year. If the calculated age is less than 1920, print: "Error, need at least 1920 year value". Example: If the following arguments are passed to your "HappyBirthday" function: "2000 Larry", your program should print: "Happy 23rd Birthday Larry!".

def happy_birthday(year: int, name: str): 
    if year < 1920:
        print("error: The year needs to be at least 1920.  You are too old for this game.  ")
        age = 2024 - year
        last_digit = age % 10
        if last_digit ==  1:
            age_str = f"{age}st"
        elif last_digit == 2:
            age_str = f"{age}nd"
        elif last_digit == 3:
            age_str = f"{age}rd"
        else:
            age_str = f"{age}th"
            print(f"Happy {age_str} Birthday,{name}! ")
            













# Write your own function named "greeting_with_gender" that accepts two parameters: "name" (string) and "gender" (string). Prints a customized greeting based on the "gender" parameter:

# If "gender" is "male", print: "Hello, Mr. {name}! Welcome!", where "{name}" is replaced with the value of the "name" parameter.
# If "gender" is "female", print: "Hello, Mrs. {name}! Welcome!", where "{name}" is replaced with the value of the "name" parameter.
# If "gender" is anything other than "male" or "female", print: "Hello, {name}! Welcome!", where "{name}" is replaced with the value of the "name" parameter.
            
            def greeting_with_gender(name: str, gender: str):
                if gender == "male":
                    print(f"Hello, Mr. {name}! Welcome!")
                elif gender == "female":
                    print(f"Hello, Mrs. {name} ! Welcome!")
                else:
                    print(f"Hello, {name}! Welcome! ")

                    print(greeting_with_gender("Bob Loblaw" , "Potato" ))







