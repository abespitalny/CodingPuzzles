'''
Given the radius and x-y positions of the center of a circle,
write a function randPoint which generates a uniform random point in the circle.

Note:
- input and output values are in floating-point.
- radius and x-y position of the center of the circle is passed into the class constructor.
- a point on the circumference of the circle is considered to be in the circle.
- randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
'''
from leetcode import *

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # THIS IS WRONG!!!!!!
        # # Generate random angle and radius:
        # rand_angle = 2 * math.pi * random.random()
        # rand_radius = self.radius * random.random()
        # # Convert random polar coordinates to random x-y coordinates:
        # return [self.x_center + (rand_radius * math.cos(rand_angle)), self.y_center + (rand_radius * math.sin(rand_angle))]

        # Using the correct mathematics:
        rand_angle = 2 * math.pi * random.random()
        rand_radius = math.sqrt((self.radius**2) * random.random())
        return [self.x_center + (rand_radius * math.cos(rand_angle)), self.y_center + (rand_radius * math.sin(rand_angle))]

# Take a look at the notes associated with this problem in the notes folder.

obj = Solution(1, 0, 0)
print(obj.randPoint(), obj.randPoint(), obj.randPoint())
obj = Solution(10, 5, -7.5)
print(obj.randPoint(), obj.randPoint(), obj.randPoint())
