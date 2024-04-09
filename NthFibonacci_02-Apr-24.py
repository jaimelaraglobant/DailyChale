# A Fibonacci sequence is a list of numbers that begins with 0 and, and each subsequent number is the sum of the previous two.
#  * For example, the first five Fibonacci numbers are:
#    0 1 1 2 3
#   If n were 4, your function should return 3; for 5, it should return 5
#  * Write a function that accepts a number, n, and returns the nth Fibonacci number. Use a recursive solution to this problem; if you finish with time left over, implement an iterative solution.
import random

def fibonacci(n):
    f = [0] * (n + 2)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

# Example usage:
n = random.randint(1,100)
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
