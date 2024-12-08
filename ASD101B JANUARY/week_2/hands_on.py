def print_backwards(iter):
    for item in iter.__reversed__():
        print(item)

try:
    file = open(r"./Week_2/states.txt", 'r')
except FileNotFoundError as err:
    print(err)
    exit()

states = []
for line in file:
    line = line.rstrip("\n")
    state = line.split()[1:]
    print(line.split())
    states.append(state)

file.close()

print_backwards(states)


    


  
