from typing import List

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# This is an utterly brilliant O(n) solution.
def singleNumber(nums: List[int]) -> int:
    # This variable will hold the solution after iterating over the list:
    ans = 0
    for n in nums:
        ans ^= n
    return ans

print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1, 0, 1]))
print(singleNumber([1, 3, 1, -1, 3]))