'''
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2),
where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.
Note: they overlap even if the circle and rectangle meet at a single point.
'''
# Time: O(1), Space: O(1).
def check_overlap(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    # Check if circle's center within left and right edges of rectangle:
    if x_center >= x1 and x_center <= x2:
        # Check if circle is within rectangle:
        if y_center >= y1 and y_center <= y2:
            return True
        # Otherwise, check if circle's center is at most a distance of radius away from either the top or bottom edges.
        return min(abs(y2 - y_center), abs(y1 - y_center)) <= radius
    # Check if circle's center is within top and left edges of rectangle:
    elif y_center >= y1 and y_center <= y2:
        # If so, check if circle's center is at most a distance of radius away from either the left or right edges.
        return min(abs(x2 - x_center), abs(x1 - x_center)) <= radius
    else:
        # Get the one of the 4 corners that is closest to the circle's center:
        x_corner = x1 if x_center < x1 else x2
        y_corner = y1 if y_center < y1 else y2
        # Check if the rectangle's closest corner is within the circle or not:
        return ((x_corner - x_center)**2 + (y_corner - y_center)**2) <= radius**2

# Another very clever Leetcode solution:
def check_overlap_v2(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    # Find the nearest point on the rectangle to the center of the circle
    x_nearest = max(x1, min(x_center, x2))
    y_nearest = max(y1, min(y_center, y2))

    # Find the distance between the nearest point and the center of the circle
    return ((x_nearest - x_center)**2 + (y_nearest - y_center)**2) <= radius**2
# My solution does basically this but in a much more verbose and ugly way. This is beautiful!


# Expected: True
print(check_overlap(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
# Expected: True
print(check_overlap(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))
# Expected: True
print(check_overlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))
# Expected: False
print(check_overlap(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
# Expected: True
print(check_overlap(radius = 24, x_center = 13, y_center = 1, x1 = 0, y1 = 15, x2 = 5, y2 = 18))

print(check_overlap_v2(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
print(check_overlap_v2(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))
print(check_overlap_v2(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))
print(check_overlap_v2(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
print(check_overlap_v2(radius = 24, x_center = 13, y_center = 1, x1 = 0, y1 = 15, x2 = 5, y2 = 18))
