'''
Given an array of integers nums, sort the array in ascending order.
'''
from leetcode import *

class Solution:
    # Iterative merge sort
    # Time: O(n*log(n))
    # Space: O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        stride = 1
        while stride < len(nums):
            for i in range(0, len(nums), 2*stride):
                left = i
                leftEnd = right = i + stride
                rightEnd = min(i + 2*stride, len(nums))
                mergedArray = []
                while left < leftEnd and right < rightEnd:
                    if nums[left] <= nums[right]:
                        mergedArray.append(nums[left])
                        left += 1
                    else:
                        mergedArray.append(nums[right])
                        right += 1
                
                if left < leftEnd:
                    mergedArray.extend(nums[left:leftEnd])
                elif right < rightEnd:
                    mergedArray.extend(nums[right:rightEnd])
                
                for j in range(len(mergedArray)):
                    nums[i + j] = mergedArray[j]

            stride *= 2
        return nums

solution = Solution()

# Expected: [1,2,3,5]
print(solution.sortArray([5,2,3,1]))

# Expected: [0,0,1,1,2,5]
print(solution.sortArray([5,1,1,2,0,0]))
