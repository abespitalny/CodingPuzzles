'''
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:
    - The number of soldiers in row i is less than the number of soldiers in row j.
    - Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
'''
from leetcode import *

# Time: O(m*(n + log(m))).
# Space: O(m).
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiersPerRow = []
        for i in range(len(mat)):
            numSoldiers = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    break
                numSoldiers += 1
            soldiersPerRow.append((i, numSoldiers))
        
        soldiersPerRow.sort(key=lambda x:x[1])
        return [soldiersPerRow[i][0] for i in range(k)]

solution = Solution()

# Expected: [2, 0, 3]
print(solution.kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k = 3))

# Expected: [0, 2]
print(solution.kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], k = 2))
