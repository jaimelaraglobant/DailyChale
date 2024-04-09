import random

def calculate_ratios(arr):
    # Initialize counters for positive, negative, and zero elements
    pos_count = 0
    neg_count = 0
    zero_count = 0

    # Iterate through the array
    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1

    # Calculate the ratios
    total_elements = len(arr)
    pos_ratio = pos_count / total_elements
    neg_ratio = neg_count / total_elements
    zero_ratio = zero_count / total_elements

    # Print the ratios with 6 decimal places
    print(f"{pos_ratio:.6f} // positive")
    print(f"{neg_ratio:.6f} // negative")
    print(f"{zero_ratio:.6f} // zero")

random_list = [random.uniform(-9, 9) for _ in range(5)]
print(random_list)

# Example usage:
arr = random_list
calculate_ratios(arr)
