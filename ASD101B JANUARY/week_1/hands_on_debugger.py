z=0

def func():
    global z
    x = float(input('Enter a number: '))
    y = float(input('Enter a number: '))
    z = (x+y)/2
   
func()
print('The average of the two numbers you have entered is: ', z)