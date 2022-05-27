'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
'''
from leetcode import *

class Solution:
    # Hashmap approach. There's a more efficient version of this that uses just a frequency table, so we don't need a set for the pairs.
    # Time: O(n)
    # Space: O(n)
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        numsSet = set([nums[0]])
        for i in range(1, len(nums)):
            otherNum = nums[i] - k
            if otherNum in numsSet:
                pairs.add((otherNum, nums[i]))
            
            otherNum = nums[i] + k
            if otherNum in numsSet:
                pairs.add((nums[i], otherNum))

            numsSet.add(nums[i])

        return len(pairs)

solution = Solution()

# Expected: 2
print(solution.findPairs(nums = [3,1,4,1,5], k = 2))

# Expected: 4
print(solution.findPairs(nums = [1,2,3,4,5], k = 1))

# Expected: 1
print(solution.findPairs(nums = [1,3,1,5,4], k = 0))
