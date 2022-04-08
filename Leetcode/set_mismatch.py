'''
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''
from leetcode import *

# Time: O(n)
# Space: O(n)
# There are two very smart solutions on Leetcode that use O(1) space:
# 1) We modify the original array. For a given number, we treat it as an index in the array and take the negative of the number at that index.
#    The duplicate number would be inverting an already negative number and the missing number would be the only number in the array that's still positive.
# 2) XOR 1..n and the given numbers which gives (missing number)^(repeated number).
#    To separate these two numbers, we separate the numbers in 1..n and nums by whether the location of the rightmost one bit in
#    (missing number)^(repeated number) is 1 or 0. Then, we XOR both of these partitions to get missing number and repeated number.
#    An example would example everything :)
#    [1,2,4,4,5,6]
#    [1,2,3,4,5,6]
#    3^4 = 7 = 111
#    Partition and XOR numbers with matching rightmost one bit location being 1/0:
#    For nums: 1^5 and 2^4^4^6
#    For 1..n: 1^3^5 and 2^4^6
#    XOR partitions: (1^5)^(1^3^5) = 3 and (2^4^4^6)^(2^4^6) = 4
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        targetSum = n*(n+1) // 2
        actualSum = 0
        table = set()
        for num in nums:
            if num in table:
                repeatedNum = num
            else:
                table.add(num)
            actualSum += num

        return [repeatedNum, repeatedNum + (targetSum - actualSum)]

solution = Solution()

# Expected: [2,3]
print(solution.findErrorNums([1,2,2,4]))

# Expected: [1,2]
print(solution.findErrorNums([1,1]))
