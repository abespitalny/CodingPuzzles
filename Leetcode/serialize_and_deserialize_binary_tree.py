from leetcode import *

# Level order representation approach similar to how Leetcode represents trees.
# Time: O(n) for both operations where n is the number of nodes in the tree.
# Space: O(n) for both operations where n is the number of nodes in the tree.
# From Leetcode, you could also do a preorder DFS representation, but I think this one is more natural.
class Codec:

    def serialize(self, root):
        if root is None:
            return '[]'

        queue = deque([root])
        levelOrder = []
        while len(queue) != 0:
            levelLen = len(queue)
            for i in range(levelLen):
                node = queue.popleft()
                if node is None:
                    levelOrder.append(None)
                    continue
                levelOrder.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                else:
                    queue.append(None)
                
                if node.right != None:
                    queue.append(node.right)
                else:
                    queue.append(None)

        # Get rid of trailing null values.
        while len(levelOrder) != 0 and levelOrder[-1] is None:
            levelOrder.pop()

        return str(levelOrder)

    def deserialize(self, data):
        levelOrder = data[1:-1].split(', ')
        if len(levelOrder[0]) == 0:
            return None

        root = TreeNode(int(levelOrder[0]))
        queue = deque([root])
        idx = 1
        while len(queue) != 0 and idx < len(levelOrder):
            node = queue.popleft()

            if levelOrder[idx] != 'None':
                node.left = TreeNode(int(levelOrder[idx]))
                queue.append(node.left)
            
            if (idx + 1) == len(levelOrder):
                break

            if levelOrder[idx + 1] != 'None':
                node.right = TreeNode(int(levelOrder[idx + 1]))
                queue.append(node.right)
            
            idx += 2
        return root

serializer = Codec()

print_bin_tree_bfs(serializer.deserialize(serializer.serialize(construct_bin_tree_bfs_array([1,2,3,None,None,4,5]))))
print_bin_tree_bfs(serializer.deserialize(serializer.serialize(construct_bin_tree_bfs_array([]))))
