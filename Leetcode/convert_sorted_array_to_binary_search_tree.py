'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''
from leetcode import *

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(log(n)) for the recursive stack
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            if end < start:
                return None
            elif start == end:
                return TreeNode(nums[start])

            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)

            return root
        
        return helper(0, len(nums) - 1)
