from leetcode import *

# Time: O(n^2).
# Space: O(n).
# This solution is very slow. There are O(n^2) solutions that are faster. Get the frequency of the numbers and then use combinatorics (see Leetcode)!
class Solution:
    def twoSumMulti(self, arr: List[int], start: int, target: int) -> int:
        numCounts = {arr[start]: 1}
        numSums = 0
        for i in range(start + 1, len(arr)):
            diff = target - arr[i]
            if diff in numCounts:
                numSums += numCounts[diff]
            numCounts[arr[i]] = numCounts.get(arr[i], 0) + 1
        return numSums

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        numSums = 0
        for i in range(len(arr) - 1):
            numSums += self.twoSumMulti(arr, i + 1, target - arr[i])
        
        return numSums % (10**9 + 7)

solution = Solution()

# Expected: 20
print(solution.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))

# Expected: 12
print(solution.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))
