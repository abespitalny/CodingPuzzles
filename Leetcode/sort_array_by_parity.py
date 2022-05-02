from leetcode import *

# Time: O(n)
# Space: O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenPtr = curPtr = 0
        while curPtr < len(nums):
            if nums[curPtr] % 2 == 0:
                nums[curPtr], nums[evenPtr] = nums[evenPtr], nums[curPtr]
                evenPtr += 1
            curPtr += 1
        return nums

solution = Solution()

# Expected: [2,4,3,1]
print(solution.sortArrayByParity([3,1,2,4]))

# Expected: [0]
print(solution.sortArrayByParity([0]))
