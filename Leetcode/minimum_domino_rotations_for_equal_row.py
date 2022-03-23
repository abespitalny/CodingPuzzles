'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
'''
from leetcode import *

# Time: O(n).
# Space: O(1).
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        minRotations = math.inf

        # Find rotations for top.
        rotations = self.dominoRotations(tops[0], tops, bottoms)
        # This is the minimal rotations you can ever get!
        if rotations == 0:
            return rotations
        elif rotations < minRotations:
            minRotations = rotations
        
        # Find rotations for bottom.
        rotations = self.dominoRotations(bottoms[0], bottoms, tops)
        if rotations == 0:
            return rotations
        elif rotations < minRotations:
            minRotations = rotations
        
        if minRotations == 1:
            return minRotations
        
        if tops[0] != bottoms[0]:
            # Swap first domino and then try to find the minimum number of subsequent rotations.
            rotations = 1 + self.dominoRotations(bottoms[0], tops, bottoms)
            if rotations < minRotations:
                minRotations = rotations

            rotations = 1 + self.dominoRotations(tops[0], bottoms, tops)
            if rotations < minRotations:
                minRotations = rotations
        
        return -1 if minRotations == math.inf else minRotations
    
    def dominoRotations(self, firstTopDomino: int, tops: List[int], bottoms: List[int]) -> int:
        rotations = 0
        for i in range(1, len(bottoms)):
            if tops[i] != firstTopDomino:
                if bottoms[i] != firstTopDomino:
                    rotations = math.inf
                    break
                else:
                    rotations += 1
        return rotations

solution = Solution()

# Expected: 2
print(solution.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))

# Expected: -1
print(solution.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))
