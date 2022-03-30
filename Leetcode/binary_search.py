from leetcode import *

# Time: O(log(n)).
# Space: O(1).
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                return mid
        return -1

solution = Solution()

# Expected: 4
print(solution.search(nums = [-1,0,3,5,9,12], target = 9))

# Expected: -1
print(solution.search(nums = [-1,0,3,5,9,12], target = 2))
