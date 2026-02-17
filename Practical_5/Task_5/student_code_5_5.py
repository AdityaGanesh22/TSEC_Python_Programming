# Rno: <student roll number>
# student_code_5_5.py

# Scientific Debugging Techniques
# Task: Implement a binary search algorithm.
# The provided code contains multiple logic and runtime errors.
# Students must apply scientific debugging techniques (like binary search debugging)
# to identify and resolve the issues methodically.

# Instructions:
# - Do not rename the function binary_search.
# - Use debugging strategies to locate and fix errors.
# - The function should return the index of the target if found, else -1.

def binary_search(arr, target):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid - 1
    return None