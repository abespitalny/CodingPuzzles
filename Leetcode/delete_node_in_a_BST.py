'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
    1. Search for a node to remove.
    2. If the node is found, delete the node.
'''
from leetcode import *

class Solution:
    # Iterative solution
    # Time: O(H) where H is the height of the tree. Average-case it's O(log(N)).
    # Space: O(1).
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prevNode = None
        curNode = root
        while curNode != None:
            if curNode.val == key:
                break

            prevNode = curNode
            if curNode.val < key:
                curNode = curNode.right
            else:
                curNode = curNode.left

        if curNode is None:
            return root

        nextNode = curNode.right if curNode.right != None else curNode.left
        
        if prevNode != None:
            if prevNode.left == curNode:
                prevNode.left = nextNode
            else:
                prevNode.right = nextNode
        else:
            root = nextNode

        node = nextNode
        if node != None and node != curNode.left:
            while node.left != None:
                node = node.left
            node.left = curNode.left
        return root

    # From Leetcode, there's also a beautiful recursive solution that has same time complexity with O(H) space complexity.
    #
    # If key > root.val then delete the node to delete is in the right subtree root.right = deleteNode(root.right, key).
    # If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key).
    # If key == root.val then the node to delete is right here. Let's do it:
    #   If the node is a leaf, the delete process is straightforward:
    #       root = null.
    #   If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val).
    #   If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).
    # Return root.
