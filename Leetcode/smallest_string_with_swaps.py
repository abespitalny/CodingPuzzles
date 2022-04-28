from leetcode import *

# Time: O(m + n*log(n)) where m is the number of pairs and n is the length of the string.
# Space: O(m + n).
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        swapsMap = {}
        for i, j in pairs:
            if i in swapsMap:
                swapsMap[i].add(j)
            else:
                swapsMap[i] = set([j])

            if j in swapsMap:
                swapsMap[j].add(i)
            else:
                swapsMap[j] = set([i])

        paths = []
        visited = set()
        for i in swapsMap:
            if i in visited:
                continue
            
            path = set()
            stack = [i]
            while len(stack) != 0:
                index = stack.pop()
                path.add(index)
                visited.add(index)
                
                if index in swapsMap:
                    for j in swapsMap[index]:
                        if j not in path:
                            stack.append(j)
            paths.append(path)

        answer = [None]*len(s)
        for i in range(len(paths)):
            pathIndices = [j for j in paths[i]]
            pathStr = [s[j] for j in paths[i]]
            pathIndices.sort()
            pathStr.sort()

            for j in range(len(paths[i])):
                answer[pathIndices[j]] = pathStr[j]

        for i in range(len(answer)):
            if answer[i] is None:
                answer[i] = s[i]
        return ''.join(answer)

solution = Solution()

# Expected: bacd
print(solution.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))

# Expected: abcd
print(solution.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))

# Expected: abc
print(solution.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))
