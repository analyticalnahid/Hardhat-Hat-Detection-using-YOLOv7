
from numpy import random
 
names = ['nahidul','yousuf','arman']
 
colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]
print(colors)
 