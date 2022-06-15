'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...].
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list,
which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

buildings is sorted by lefti in non-decreasing order.
'''
from leetcode import *

class Solution:
    # Divide and Conquer approach.
    # Time: O(n*log(n))
    # Space: O(n)
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        mid = len(buildings) // 2
        leftSkyline = self.getSkyline(buildings[:mid])
        rightSkyline = self.getSkyline(buildings[mid:])

        mergedSkyline = []
        leftHeight = 0
        rightHeight = 0
        i = 0
        j = 0
        sweep = leftSkyline[0][0]
        end = max(leftSkyline[-1][0], rightSkyline[-1][0])
        while sweep < end:
            if i < len(leftSkyline) and sweep == leftSkyline[i][0]:
                leftHeight = leftSkyline[i][1]
                i += 1
            if j < len(rightSkyline) and sweep == rightSkyline[j][0]:
                rightHeight = rightSkyline[j][1]
                j += 1

            height = max(leftHeight, rightHeight)
            if len(mergedSkyline) == 0 or height != mergedSkyline[-1][1]:
                mergedSkyline.append([sweep, height])

            if i < len(leftSkyline) and j < len(rightSkyline):
                sweep = min(leftSkyline[i][0], rightSkyline[j][0])
            elif i < len(leftSkyline):
                sweep = leftSkyline[i][0]
            else:
                sweep = rightSkyline[j][0]

        mergedSkyline.append([end, 0])
        return mergedSkyline


solution = Solution()

# Expected: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))

# Expected: [[0,3],[5,0]]
print(solution.getSkyline([[0,2,3],[2,5,3]]))
