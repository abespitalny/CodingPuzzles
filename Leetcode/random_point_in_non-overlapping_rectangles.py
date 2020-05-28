'''
Given a list of non-overlapping axis-aligned rectangles rects,
write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:
- An integer point is a point that has integer coordinates. 
- A point on the perimeter of a rectangle is included in the space covered by the rectangles.
- ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner,
and [x2, y2] are the integer coordinates of the top-right corner.
- pick return a point as an array of integer coordinates [p_x, p_y]
'''
from leetcode import *

class Solution:
    # We assume that there is at least one rectangle in the list.
    # Time: O(|rects|), Space: O(|rects|).
    # We must iterate through all the rectangles in order to obtain the total number of points
    # and we must use O(|rects|) space in order to save the numbers of points in the rectangles.
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # This is the total number of points:
        total_num_points = 0
        # The number of points of all the rectangles except the last one:
        nums_points = []
        num_rects = len(rects)
        for i in range(num_rects):
            r = rects[i]
            # We are adding 1 to the difference because the random point can be on the boundary of the rectangle.
            num_points = (r[2] - r[0] + 1) * (r[3] - r[1] + 1)
            total_num_points += num_points
            if i < (num_rects - 1):
                nums_points.append(total_num_points)

        self.total_num_points = total_num_points
        self.nums_points = nums_points

    # Time: O(log(|rects|)) to pick a rectangle, Space: O(1).
    def pick(self) -> List[int]:
        # Pick which rectangle to choose point from:
        rand_rect = self.total_num_points * random.random()

        # Search for the last element in the list that is greater than rand_rect in O(log(|rects|)) time:
        nums_points = self.nums_points
        start = 0
        end = len(nums_points) - 1
        # By default we choose the last rectangle:
        rect_ind = len(nums_points)
        while start <= end:
            mid = (start + end) // 2
            if rand_rect < nums_points[mid]:
                rect_ind = mid
                end = mid - 1
            else:
                start = mid + 1

        # Choose the x-y coordinates from the picked rectangle:
        rect = self.rects[rect_ind]
        x_coord = int((rect[2] - rect[0] + 1) * random.random()) + rect[0]
        y_coord = int((rect[3] - rect[1] + 1) * random.random()) + rect[1]
        return [x_coord, y_coord]

# A simple summation of my algorithm:
# 1) randomly sample the rectangles weighted by the area
# 2) randomly sample the integer points given a rectangle is selected

obj = Solution([[1,1,5,5]])
print(obj.pick())
print(obj.pick())
print(obj.pick())

obj = Solution([[-2,-2,-1,-1],[1,0,3,0]])
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())

# THIS CODE WAS USED TO DEBUG THE PROGRAM:
# I generated 10,000 random points and checked if the resulting histogram displayed a uniform distribution across all the points.

# obj = Solution([[82918473, -57180867, 82918476, -57180863], [83793579, 18088559, 83793580, 18088560], [66574245, 26243152, 66574246, 26243153], [72983930, 11921716, 72983934, 11921720]])
# freq = {}
# for i in range(10000):
#     rand_point = tuple(obj.pick())
#     freq[rand_point] = freq.get(rand_point, 0) + 1

# import matplotlib.pyplot as plt
# points = []
# freqs = []
# for i, j in enumerate(freq):
#     points.append(i)
#     freqs.append(freq[j])

# plt.bar(points, freqs)
# plt.show()