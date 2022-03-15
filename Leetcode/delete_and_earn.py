'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
    - Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.
'''
from leetcode import *

# Time: O(n*log(n)) because we sort the array of nums.
# Space: O(n) for storing the counts of nums.
# Note: this problem is similar to house robber problem.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            count = counts.get(i, 0) + i
            counts[i] = count
        
        sortedNums = list(counts.items())
        sortedNums.sort(key=lambda x:x[0])

        maxNumPoints = [0, sortedNums[0][1]]
        for i in range(1, len(sortedNums)):
            numCount = sortedNums[i]
            if numCount[0] > (sortedNums[i - 1][0] + 1):
                nextMaxNumPoints = maxNumPoints[1] + numCount[1]
            else:
                nextMaxNumPoints = max(maxNumPoints[1], maxNumPoints[0] + numCount[1])
            maxNumPoints[0] = maxNumPoints[1]
            maxNumPoints[1] = nextMaxNumPoints
        return maxNumPoints[-1]

solution = Solution()

# Expeceted: 6
print(solution.deleteAndEarn([3,4,2]))

# Expeceted: 9
print(solution.deleteAndEarn([2,2,3,3,3,4]))
