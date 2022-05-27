'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
from leetcode import *

class Solution:
    # Recursion approach.
    # Time: O(n!) <= sum of P(n, k) where k goes from 1 to n <= O(n * n!)
    # Space: O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        perms = []
        prevPerms = self.permute(nums[1:])
        for i in range(len(prevPerms)):
            prevPerm = prevPerms[i]
            for j in range(len(prevPerm) + 1):
                perm = prevPerm.copy()
                perm.insert(j, nums[0])
                perms.append(perm)
        return perms

    # From Leetcode, there's a nice backtracking approach. Same runtime and space complexity as the other approach though this probably uses generally less space.
    def permute2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])

            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack(0)
        return output


solution = Solution()

# Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(solution.permute([1,2,3]))

# Expected: [[0,1],[1,0]]
print(solution.permute([0, 1]))

# Expected: [[1]]
print(solution.permute([1]))
