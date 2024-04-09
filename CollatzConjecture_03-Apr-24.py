# Let n be a positive integer number, if you apply the following rules, eventually you will reach to 1:
# If n is even  then divide by 2. If n is odd then multiply by 3 and add 1.
import random

def collatz(n):
    def step(n, steps, sequence):
        if n == 1:
            return {"steps": steps, "sequence": sequence + [1]}
        elif n % 2 == 0:
            return step(n // 2, steps + 1, sequence + [n])
        else:
            return step(3 * n + 1, steps + 1, sequence + [n])

    # Initialize with empty sequence and zero steps
    result = step(n, 0, [])

    return result

#usage:
initial_number =  random.randint(1,99)
print("Initial Number: ", initial_number)

collatz_result = collatz(initial_number)
print(f"Starting from {initial_number}, it took {collatz_result['steps']} steps.")
print(f"Sequence of values: {collatz_result['sequence']}")
