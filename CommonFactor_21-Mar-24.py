import random
from math import gcd 

def common_factors(num1, num2):
    n = []
    g = gcd(num1, num2)
    print( "Greatest Common Factor: ", g)
    for i in range(1, g + 1):
        if g % i == 0:
            n.append(i)
    return n

num1 = random.randint(1,99) 
num2 = random.randint(1,99) 
result = common_factors(num1, num2)
print("Common factors of", num1, "and", num2, "are:", result)