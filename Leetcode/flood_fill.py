'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
'''
from leetcode import *

class Solution:
    # Time: O(m*n)
    # Space: O(m*n)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        image[sr][sc] = newColor
        stack = [(sr, sc)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(stack) != 0:
            r, c = stack.pop()

            for i, j in directions:
                i += r
                j += c
                
                if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != oldColor:
                    continue

                image[i][j] = newColor
                stack.append((i, j))
        return image

solution = Solution()

# Expected: [[2,2,2],[2,2,0],[2,0,1]]
print(solution.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))

# Expected: [[2,2,2],[2,2,2]]
print(solution.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2))
