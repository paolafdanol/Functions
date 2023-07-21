print("\n      Números aleatorios\n")

import random

print("---Random")
for i in range(10):
    x = random.random()
    print(x)

print("\n---Randint")
a = random.randint(5, 10)
print(a)

print("\n---Random Choice")
t = [1,2,3]
b = random.choice(t)
print(b)