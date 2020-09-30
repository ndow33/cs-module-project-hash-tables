import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
d = {}
d[0] = {}
d[0][0] = 1
print(math.factorial(5))

print(d)
print(d[0][0])
