keep_going = True
while keep_going:
  sugar = input("Add sugar? (yes/no):")
while sugar not in {'yes', 'no'}:
        print("You must answer yes or no.")
        sugar = input(" Add sugar? (yes/no):")
        keep_going = sugar == "yes"
        