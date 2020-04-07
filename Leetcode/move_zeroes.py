from typing import List

def move_zeroes(nums: List[int]) -> None:
    nums_len = len(nums)
    j = 0
    for i in range(nums_len):
        if nums[j] == 0:
            nums.pop(j)
            nums.append(0)
            j -= 1
        j += 1

arr = [0, 1, 0, 3, 12]
move_zeroes(arr)
print(arr)
arr = [0, 0, 1]
move_zeroes(arr)
print(arr)