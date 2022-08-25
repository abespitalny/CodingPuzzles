'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance.

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
from leetcode import *

class Solution:
    # Quickselect algorithm
    # Time: O(n) on average and O(n^2) in worst case.
    # Space: O(log(n)) on average and O(n) in worst case.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        
        def partition(left, right):
            pivot = random.randint(left, right)

            pivotDist = (points[pivot][0]**2) + (points[pivot][1]**2)
            points[right], points[pivot] = points[pivot], points[right]
            
            tempPivot = left
            for i in range(left, right):
                dist = (points[i][0]**2) + (points[i][1]**2)
                if dist <= pivotDist:
                    points[i], points[tempPivot] = points[tempPivot], points[i]
                    tempPivot += 1
            
            points[tempPivot], points[right] = points[right], points[tempPivot]
            return tempPivot


        def select(left, right):
            if left == right:
                return left
            
            pivot = partition(left, right)
            
            if k < pivot:
                select(left, pivot - 1)
            elif k > pivot:
                select(pivot + 1, right)
            else:
                return

        select(0, len(points) - 1)
        return points[:k]

solution = Solution()

# Expected: [[-2,2]]
print(solution.kClosest(points = [[1,3],[-2,2]], k = 1))
# Expected: [[3,3],[-2,4]]
print(solution.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
