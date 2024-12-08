# 1. Write a statement that creates a dictionary containing the following key-value pairs:

#  'a' : 1
#  'b' : 2
#   'c' : 3

my_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
    



# 3. Assume the variable dct references a dictionary. Write an if statement that determines whether the key 'James' exists in the dictionary. If so, display the value that is associated with that key. If the key is not in the dictionary, display a message indicating so.
dct = {
    "James" : 1,
    "Bob" : 2

}
if "James" in dct:
    print(dct["James"])
else:
    print("The key 'James' is not in the dictionary")

