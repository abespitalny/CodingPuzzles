'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.
'''
from leetcode import *

class Solution:
    # Line equation approach. There might also be an approach involving the cross product.
    # Time: O(n) where n is the number of points.
    # Space: O(1)
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:        
        # Express the line equation y = mx + b as:
        # (y1 - y2)*x + (x2 - x1)*y = (y1*x2 - y2*x1)
        # Ax + By = C
        A = coordinates[0][1] - coordinates[1][1]
        B = coordinates[1][0] - coordinates[0][0]
        C = (coordinates[0][1]*coordinates[1][0]) - (coordinates[1][1]*coordinates[0][0])
        
        for i in range(2, len(coordinates)):
            leftHandSide = (A*coordinates[i][0]) + (B*coordinates[i][1])
            if leftHandSide != C:
                return False
        return True

solution = Solution()

assert solution.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True
assert solution.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False
