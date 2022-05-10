from leetcode import *

class Solution:
    # Greedy approach
    # Time: O(n)
    # Space: O(n)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minRight = [0]*len(nums)
        minRight[-1] = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            minRight[i] = min(minRight[i + 1], nums[i])
        
        maxLeft = [0]*len(nums)
        maxLeft[0] = nums[0]
        for i in range(1, len(nums)):
            maxLeft[i] = max(maxLeft[i - 1], nums[i])

        leftIdx = 0
        for i in range(len(nums)):
            if nums[i] <= minRight[i]:
                leftIdx += 1
            else:
                break

        rightIdx = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] >= maxLeft[i]:
                rightIdx -= 1
            else:
                break

        if leftIdx > rightIdx:
            return 0
        return (rightIdx - leftIdx + 1)
        
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minRight = [0]*len(nums)
        minRight[-1] = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            minRight[i] = min(minRight[i + 1], nums[i])
        
        maxLeft = [0]*len(nums)
        maxLeft[0] = nums[0]
        for i in range(1, len(nums)):
            maxLeft[i] = max(maxLeft[i - 1], nums[i])

        leftIdx = 0
        for i in range(len(nums)):
            if nums[i] <= minRight[i]:
                leftIdx += 1
            else:
                break

        rightIdx = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] >= maxLeft[i]:
                rightIdx -= 1
            else:
                break

        if leftIdx > rightIdx:
            return 0
        return (rightIdx - leftIdx + 1)
    
    # Time: O(n).
    # Space: O(1).
    # This is a modified version of the above greedy approach with only 2 loops and O(1) space! There is a less readable version with only one loop.
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        maxNum = nums[0]
        rightIdx = 0
        for i in range(1, len(nums)):
            if nums[i] < maxNum:
                rightIdx = i
            else:
                maxNum = nums[i]

        minNum = nums[-1]
        leftIdx = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > minNum:
                leftIdx = i
            else:
                minNum = nums[i]

        return 0 if (rightIdx - leftIdx) <= 0 else (rightIdx - leftIdx + 1)

solution = Solution()

# Expected: 5
print(solution.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(solution.findUnsortedSubarray2([2,6,4,8,10,9,15]))

# Expected: 0
print(solution.findUnsortedSubarray([1,2,3,4]))
print(solution.findUnsortedSubarray2([1,2,3,4]))

# Expected: 0
print(solution.findUnsortedSubarray([1]))
print(solution.findUnsortedSubarray2([1]))
