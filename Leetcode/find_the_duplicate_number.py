'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Follow up:
    - Can you solve the problem in linear runtime complexity?
'''
from leetcode import *

# Time: O(n), Space: O(n). Solution didn't satisfy problem constraints.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = set()
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return nums[i]
            hashtable.add(nums[i])

# Had to look at solutions on leetcode.
# There are several good approaches.
# 1) Binary search
#    Binary search on the range 1..n and for each number iterate through nums to get the count of the numbers <= to that number.
#    The duplicate is the smallest number where the count exceeds the number.
#    Runs in O(n*log(n)) with O(1) space.
# 2) Count the number of ones in each bit position for nums and for 1..n then subtract the two. This'll give you the duplicate. Runs in O(n*log(n)) with O(1) space.
# 3) This is the most ingenious solution! Turn the array into a linked list where the number at that position points to nums[nums[i]]. There will be a cycle and the
#    start of the cycle is the duplicate number, so we can use a modified solution to Linked List Cycle II to find the start of the cycle. Can be done in O(n) time and O(1) space.
