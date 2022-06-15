'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
'''
from leetcode import *

class Solution:
    # Monotonic stack approach. There are ways to improve the efficiency a little. See Leetcode for more in-depth explanation.
    # This is a very beautiful problem.
    # Time: O(n)
    # Space: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(1, heights[0])]
        maxArea = heights[0]

        for i in range(1, len(heights)):
            if heights[i] > stack[-1][1]:
                stack.append((1, heights[i]))
            else:
                width = 0
                minHeight = math.inf

                while len(stack) != 0:
                    if heights[i] > stack[-1][1]:
                        break

                    rect = stack.pop()
                    width += rect[0]
                    minHeight = min(rect[1], minHeight)
                    maxArea = max(width * minHeight, maxArea)

                stack.append((width + 1, heights[i]))
        
        width = 0
        minHeight = math.inf
        for rect in reversed(stack):
            width += rect[0]
            minHeight = min(rect[1], minHeight)
            maxArea = max(width * minHeight, maxArea)

        return maxArea
    
    # From Leetcode, the divide and conquer approach. This gives you a time limit exceeded.
    # Time: O(n*log(n)) on average and O(n^2) in worst case where heights are sorted.
    # Space: O(n)
    def largestRectangleArea2(self, heights: List[int]) -> int:
        def helper(start, end):
            if (end - start) < 1:
                return 0
            if (end - start) == 1:
                return heights[start]

            minHeightIdx = start
            for i in range(start + 1, end):
                if heights[i] < heights[minHeightIdx]:
                    minHeightIdx = i

            largestRectLeft = helper(start, minHeightIdx)
            largestRectRight = helper(minHeightIdx + 1, end)
            
            return max(largestRectLeft, largestRectRight, (end - start) * heights[minHeightIdx])

        return helper(0, len(heights))

solution = Solution()

# Expected: 10
print(solution.largestRectangleArea([2,1,5,6,2,3]))
print(solution.largestRectangleArea2([2,1,5,6,2,3]))

# Expected: 4
print(solution.largestRectangleArea([2,4]))
print(solution.largestRectangleArea2([2,4]))
