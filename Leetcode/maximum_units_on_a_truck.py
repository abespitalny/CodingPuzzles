'''
You are assigned to put some amount of boxes onto one truck.

You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    - numberOfBoxesi is the number of boxes of type i.
    - numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
'''
from leetcode import *

class Solution:
    # Sorting + Greedy approach
    # Time: O(n*log(n)) because of the sorting plus O(n) for greedily selecting boxes with the most units.
    # Space: O(n) because of Python's sorting.
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort by number of units per box
        boxTypes.sort(key=lambda x:-x[1])
        
        numUnits = 0
        for i in range(len(boxTypes)):
            boxes, unitsPerBox = boxTypes[i]

            numUnits += (min(truckSize, boxes) * unitsPerBox)
            truckSize = max(0, truckSize - boxes)
            if truckSize == 0:
                break

        return numUnits

solution = Solution()

assert solution.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4) == 8
assert solution.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10) == 91
