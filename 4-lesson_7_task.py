from itertools import count
from math import factorial
def generator():
    for el in count(1):
        yield factorial(el)

g = generator()

i = 0
for el in g:
    if i < 10:
        print(el)
        i += 1
    else:
        break