from random import randint



a = [randint(0, 100) for x in range(10)]
b = [randint(0, 100) for x in range(10)]
print(a)
print(b)
print([x for x in a if x in b])

u = set(a).intersection(set(b))
print(u)