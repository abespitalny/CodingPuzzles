'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Follow up:
    - Can you solve the problem in linear runtime complexity?
'''
from leetcode import *

class Solution:
    # Time: O(n), Space: O(n). Solution didn't satisfy problem constraints.
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = set()
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return nums[i]
            hashtable.add(nums[i])

    # This is the most ingenious solution!
    # Turn the array into a linked list where the number at that position points to nums[nums[i]].
    # There will be a cycle and the start of the cycle is the duplicate number,
    # so we can use a modified solution to Linked List Cycle II to find the start of the cycle.
    # Time: O(n)
    # Space: O(1)
    def findDuplicate2(self, nums: List[int]) -> int:
        # Detect cycle using tortoise and hare.
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find beginning of cycle which is the repeated number.
        start = nums[0]
        while start != fast:
            start = nums[start]
            fast = nums[fast]

        return start

    # Binary search approach
    # Time: O(n*log(n))
    # Space: O(1)
    def findDuplicate3(self, nums: List[int]) -> int:
        def countLessThanNum(nums, num):
            count = 0
            for i in nums:
                if i <= num:
                    count += 1
            return count

        left = 1
        right = len(nums)
        while (left + 1) < right:
            mid = (left + right) // 2

            countNums = countLessThanNum(nums, mid)
            
            if countNums <= mid:
                left = mid
            else:
                right = mid

        if countLessThanNum(nums, left) > left:
            return left
        return right

# Had to look at solutions on leetcode.
# There are several good approaches.
# 1) Binary search
#    Binary search on the range 1..n and for each number iterate through nums to get the count of the numbers <= to that number.
#    The duplicate is the smallest number where the count exceeds the number.
#    Runs in O(n*log(n)) with O(1) space.
# 2) Count the number of ones in each bit position for nums and for 1..n then subtract the two. This'll give you the duplicate. Runs in O(n*log(n)) with O(1) space.
# 3) This is the most ingenious solution! Turn the array into a linked list where the number at that position points to nums[nums[i]]. There will be a cycle and the
#    start of the cycle is the duplicate number, so we can use a modified solution to Linked List Cycle II to find the start of the cycle. Can be done in O(n) time and O(1) space.

solution = Solution()

assert solution.findDuplicate([1,3,4,2,2]) == 2
assert solution.findDuplicate2([1,3,4,2,2]) == 2
assert solution.findDuplicate3([1,3,4,2,2]) == 2

assert solution.findDuplicate([3,1,3,4,2]) == 3
assert solution.findDuplicate2([3,1,3,4,2]) == 3
assert solution.findDuplicate3([3,1,3,4,2]) == 3

assert solution.findDuplicate3([1, 1]) == 1

