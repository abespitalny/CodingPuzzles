'''
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes),
where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.
'''
from leetcode import *

# Time: O(V + E) because this is just breadth-first search (BFS),
# Space: O(V) because of the queue used to store the nodes at each level.
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(0, root)])
        maxWidth = 0
        while len(queue) != 0:
            nodesOnLevel = len(queue)
            width = (queue[-1][0] - queue[0][0]) + 1
            
            for i in range(nodesOnLevel):
                pos, node = queue.popleft()
                
                if node.left != None:
                    queue.append((pos << 1, node.left))
                if node.right != None:
                    queue.append(((pos << 1) + 1, node.right))
            
            if width > maxWidth:
                maxWidth = width
        return maxWidth

solution = Solution()

# Expected: 4
print(solution.widthOfBinaryTree(construct_bin_tree_bfs_array([1,3,2,5,3,None,9])))

# Expected: 2
print(solution.widthOfBinaryTree(construct_bin_tree_bfs_array([1,3,None,5,3])))

# Expected: 2
print(solution.widthOfBinaryTree(construct_bin_tree_bfs_array([1,3,2,5,None,None,None])))
