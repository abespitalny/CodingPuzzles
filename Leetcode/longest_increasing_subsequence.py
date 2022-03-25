'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''
from leetcode import *

# Time: O(n*log(n)).
# Space: O(n) because the whole input array can be in the longest increasing subsequence.
# Note: we aren't building the actual longest increasing subsequence in this solution (e.g., nums = [3, 4, 5, 1]),
# but we're getting the correct length of the LIS.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lastElemSubseqs = [nums[0]]
        for i in range(1, len(nums)):
            start = 0
            end = len(lastElemSubseqs)
            while start < end:
                mid = (start + end) // 2
                if lastElemSubseqs[mid] < nums[i]:
                    start = mid + 1
                elif lastElemSubseqs[mid] > nums[i]:
                    end = mid
                else:
                    start = -1
                    break

            if start < 0:
                continue
            elif start == len(lastElemSubseqs):
                lastElemSubseqs.append(nums[i])
            else:
                lastElemSubseqs[start] = nums[i]

        return len(lastElemSubseqs)

solution = Solution()

# Expected: 4
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))

# Expected: 4
print(solution.lengthOfLIS([0,1,0,3,2,3]))

# Expected: 1
print(solution.lengthOfLIS([7,7,7,7,7,7,7]))
