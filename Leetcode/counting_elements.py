from leetcode import *

# This is an O(n) algorithm.
def count_elements(arr: List[int]) -> int:
    unique_elems = set()
    arr_size = len(arr)
    for i in range(arr_size):
        unique_elems.add(arr[i])

    count = 0
    for i in range(arr_size):
        if (arr[i] + 1) in unique_elems:
            count += 1
    return count

print(count_elements([1, 2, 3]))
print(count_elements([1, 1, 3, 3, 5, 5, 7, 7]))
print(count_elements([1, 3, 2, 3, 5, 0]))
print(count_elements([1, 1, 2, 2]))
