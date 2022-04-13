'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
from leetcode import *

# The O(n) solution on Leetcode was based on the QuickSelect algorithm which has an average runtime of O(n) and a worst case of O(n^2).
# QuickSelect is a general algorithm for finding the kth element in a sorted array in O(n) time.
class Solution:
    # Time: O(n*log(n)). We have to sort the counts to find the most frequent K numbers.
    # Space: O(n) for storing the counts.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        sortedCounts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        answer = []
        i = 0
        while i < k:
            answer.append(sortedCounts[i][0])
            i += 1
        return answer
    
    # Bucket sort algorithm.
    # Time: O(n).
    # Space: O(n).
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        numsToCounts = {}
        for i in range(len(nums)):
            numsToCounts[nums[i]] = numsToCounts.get(nums[i], 0) + 1
        
        countsToNums = {}
        for i in numsToCounts:
            someNums = countsToNums.get(numsToCounts[i], [])
            if len(someNums) == 0:
                countsToNums[numsToCounts[i]] = someNums
            someNums.append(i)
        
        answer = []
        for i in range(len(nums), 0, -1):
            if i in countsToNums:
                someNums = countsToNums[i]
                for j in someNums:
                    answer.append(j)
                    k -= 1
                    if k == 0:
                        return answer
        return answer

solution = Solution()

# Expected: [1,2]
print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

# Expected: [1]
print(solution.topKFrequent(nums = [1], k = 1))
