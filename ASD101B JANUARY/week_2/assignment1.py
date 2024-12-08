
# . Assume the list numbers1 has 100 elements, and numbers2 is an empty list. Write code that copies the values in numbers1 to numbers2.

import random


numbers1 = [random.randint(1, 1000) for i in range(100)]

numbers2 = numbers1[:]

