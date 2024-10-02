from fake_math import *
from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        result = first / second
    return result

result1 = divide(69, 3)
result4 = divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)