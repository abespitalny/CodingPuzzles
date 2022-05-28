from leetcode import *

class Solution:
    # Iterative approach
    # Time: O(n)
    # Space: O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        if root is None:
            return preorder
        
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            preorder.append(node.val)
            
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return preorder

    # Morris Traversal
    # Time: O(n) since we visit a predecessor twice only.
    # Space: O(1) if we discount the output array.
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def predecessor(root: TreeNode, child: TreeNode) -> TreeNode:
            while child.right != None and child.right != root:
                child = child.right
            return child

        node = root
        while node != None:
            if node.left != None:
                pred = predecessor(node, node.left)
                if pred.right is None:
                    output.append(node.val)
                    pred.right = node
                    node = node.left
                else:
                    pred.right = None
                    node = node.right
            else:
                output.append(node.val)
                node = node.right

        return output

solution = Solution()

# Expected: [1,2,3]
print(solution.preorderTraversal(construct_bin_tree_bfs_array([1,None,2,3,None])))
print(solution.preorderTraversal2(construct_bin_tree_bfs_array([1,None,2,3,None])))

# Expected: []
print(solution.preorderTraversal(construct_bin_tree_bfs_array([])))
print(solution.preorderTraversal2(construct_bin_tree_bfs_array([])))

# Expected: [1]
print(solution.preorderTraversal(construct_bin_tree_bfs_array([1])))
print(solution.preorderTraversal2(construct_bin_tree_bfs_array([1])))
