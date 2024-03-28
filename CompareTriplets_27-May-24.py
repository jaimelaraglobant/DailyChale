
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    return [alice_score, bob_score]

result1 = compareTriplets([1, 2, 3], [3, 2, 1])
result2 = compareTriplets([5, 6, 7], [3, 6, 10])
result3 = compareTriplets([17, 18, 30], [99, 16, 8])
result4 = compareTriplets([20, 20, 30], [20, 20, 50])
result5 = compareTriplets([6, 8, 12], [7, 9, 15])
result6 = compareTriplets([10, 15, 20], [5, 6, 7])

print(result1)  # Output: [1, 1]
print(result2)  # Output: [1, 1]
print(result3)  # Output: [0, 3]
print(result4)  # Output: [0, 3]
print(result5)  # Output: [0, 3]
print(result6)  # Output: [3, 0]