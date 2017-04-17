
# https://docs.python.org/2/library/random.html

import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.choice('abcdefghij'))


items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items)
