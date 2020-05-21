'''
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner.
'''
# Time: O(1), Space: O(1).
# I'm assuming the rectangles provided are valid.
def compute_area(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    # Area of both rectangles added together:
    rec1_width, rec1_height, rec2_width, rec2_height = (C - A), (D - B), (G - E), (H - F)
    total_area = (rec1_width * rec1_height) + (rec2_width * rec2_height)
    # Subtract the total area by the area of the intersection of the two rectangles (could be 0):
    if E <= A:
        intersection_width = min((G - A), rec1_width)
    else:
        intersection_width = min((C - E), rec2_width)
    if intersection_width <= 0:
        return total_area

    if F >= B:
        intersection_height = min((D - F), rec2_height)
    else:
        intersection_height = min((H - B), rec1_height)
    if intersection_height <= 0:
        return total_area

    return (total_area - (intersection_width * intersection_height))

# A much simpler solution from Leetcode which is also O(1):
def compute_area_v2(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    total_area = ((C - A) * (D - B)) + ((G - E) * (H - F))
    # Calculation of the intersection is subtle yet utter genius!
    intersection_height = min(C, G) - max(A, E)
    if intersection_height <= 0:
        return total_area
    intersection_width = min(H, D) - max(F, B)
    if intersection_width <= 0:
        return total_area
    return total_area - (intersection_width * intersection_height)


# Expected: 45
print(compute_area(-3, 0, 3, 4, 0, -1, 9, 2))
# Expected: 17
print(compute_area(-2, -2, 2, 2, 3, 3, 4, 4))
# Expected: 16
print(compute_area(-2, -2, 2, 2, -1, -1, 1, 1))

print(compute_area_v2(-3, 0, 3, 4, 0, -1, 9, 2))
print(compute_area_v2(-2, -2, 2, 2, 3, 3, 4, 4))
print(compute_area_v2(-2, -2, 2, 2, -1, -1, 1, 1))
