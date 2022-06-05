from leetcode import *

class Solution:
    # Time: O(4^n / sqrt(n)) because there a Catalan number of possible subtrees and that needs to be computed n times.
    # Space: O(4^n / sqrt(n)).
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left, right):
            if left > right:
                return [None]
            
            trees = []
            for i in range(left, right + 1):
                leftSubtrees = helper(left, i - 1)
                rightSubtrees = helper(i + 1, right)
                
                for l in leftSubtrees:
                    for r in rightSubtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees

        return helper(1, n)
    
    # Recursion with memoization!
    def generateTrees2(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def helper(left, right):
            if left > right:
                return [None]
            
            if (left, right) in memo:
                return memo[(left, right)]

            trees = []
            for i in range(left, right + 1):
                leftSubtrees = helper(left, i - 1)
                rightSubtrees = helper(i + 1, right)
                
                for l in leftSubtrees:
                    for r in rightSubtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            
            memo[(left, right)] = trees
            return trees

        return helper(1, n)

solution = Solution()

# Expected: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
trees = solution.generateTrees(3)
for t in trees:
    print_bin_tree_bfs(t)
print()

trees = solution.generateTrees2(3)
for t in trees:
    print_bin_tree_bfs(t)
print()

# Expected: [[1]]
trees = solution.generateTrees(1)
for t in trees:
    print_bin_tree_bfs(t)
print()

trees = solution.generateTrees2(1)
for t in trees:
    print_bin_tree_bfs(t)
