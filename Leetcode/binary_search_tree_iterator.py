from leetcode import *

class BSTIterator:
    # Time: O(H)
    # Space: O(H)
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left

    # Time: Worst case it's O(n), but the average case it's O(1).
    # Space: O(H).
    def next(self) -> int:
        node = self.stack.pop()
        ans = node.val
        if node.right != None:
            node = node.right
            while node != None:
                self.stack.append(node)
                node = node.left
        return ans

    # Time: O(1).
    # Space: O(H) where H is the height of the tree.
    def hasNext(self) -> bool:
        return (len(self.stack) > 0)

bSTIterator = BSTIterator(construct_bin_tree_bfs_array([7, 3, 15, None, None, 9, 20]))
print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext()) # return False
