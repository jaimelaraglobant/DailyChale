# Given an integer array nums, find the contiguous subarray with the largest sum, and return its sum.
import numpy as np

def maxSubArray(nums):
    max_so_far = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0

    for i, num in enumerate(nums):
        if current_sum + num < num:
            current_sum = num
            start_index = i
        else:
            current_sum += num

        if current_sum > max_so_far:
            max_so_far = current_sum
            end_index = i

    max_subarray = nums[start_index:end_index + 1]
    return max_so_far, max_subarray

# Example usage
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum1, subarray1 = maxSubArray(nums1)
print(f"Example 1: Maximum contiguous sum is {max_sum1}, subarray: {subarray1}")  # Output: 6, [4, -1, 2, 1]

nums2 = [1]
max_sum2, subarray2 = maxSubArray(nums2)
print(f"Example 2: Maximum contiguous sum is {max_sum2}, subarray: {subarray2}")  # Output: 1, [1]

nums3 = [5, 4, -1, 7, 8]
max_sum3, subarray3 = maxSubArray(nums3)
print(f"Example 3: Maximum contiguous sum is {max_sum3}, subarray: {subarray3}")  # Output: 23, [5, 4, -1, 7, 8]

min_val, max_val = -10, 10
randomsize = np.random.randint(1,15)
randomarray = np.random.randint(min_val, max_val, size=(randomsize))
print('Random Array')
print(randomarray)
max_sum4, subarray4 = maxSubArray(randomarray)
print(f"Example 4: Maximum contiguous sum is {max_sum4}, subarray: {subarray4}")