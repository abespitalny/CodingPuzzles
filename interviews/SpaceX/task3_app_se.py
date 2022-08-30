class Tree(object):
    x = 0
    l = None
    r = None

# Time complexity: O(N) where N is the number of nodes in the tree T.
# Space complexity: O(H) where H is the height of the tree T (log(N) in average case).
def solution(T):
    def dfs(root, path):
        path.add(root.x)
        pathLength = len(path)

        leftLongestPath = 0
        if (root.l != None) and (root.l.x not in path):
            leftLongestPath = dfs(root.l, path)

        rightLongestPath = 0
        if (root.r != None) and (root.r.x not in path):
            rightLongestPath = dfs(root.r, path)

        path.remove(root.x)

        return max(pathLength,leftLongestPath, rightLongestPath)

    return dfs(T, set())
