data = [1,2,4,6,2]
target = 6

import time
# Binary Search
def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Perform search
index = binary_search(data, target)
print("Index of target:", index)

