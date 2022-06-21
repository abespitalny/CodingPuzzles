'''
There is a long table with a line of plates and candles arranged on top of it.
You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive).
For each query, you need to find the number of plates between candles that are in the substring.
A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|".
The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.
'''
from leetcode import *

class Solution:
    # Binary search + prefix sum approach. You could do this in O(n + Q) time by removing the need for binary search.
    # Basically, we store the nearest candle to the left and to the right for all indices in the string s, so we can calculate the number
    # of plates between two indices in O(1) time. Got this idea from Leetcode.
    # Time: O(n + Q * log(n)) where n is the length of s and Q is the number of queries.
    # Space: O(n) for storing the indices along with the prefix sums for the candles.
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        start = 0
        while start < len(s) and s[start] != '|':
            start += 1

        # There are no candles!
        if start == len(s):
            return [0]*len(queries)
            
        candles = [(start, 0)]
        numPlates = 0
        for i in range(start + 1, len(s)):
            if s[i] == '|':
                candles.append((i, numPlates + candles[-1][1]))
                numPlates = 0
            else:
                numPlates += 1


        def binarySearch(pos):
            left = 0
            right = len(candles) - 1
            while left < right:
                mid = (left + right) // 2
                midPos = candles[mid][0]
                
                if pos == midPos:
                    return mid
                elif pos < midPos:
                    right = mid
                else:
                    left = mid + 1

            return left


        answer = []
        for i, j in queries:
            # Binary search for candle positions
            posi = binarySearch(i)
            posj = binarySearch(j)

            if j < candles[posj][0]:
                posj -= 1

            if posj <= posi:
                answer.append(0)
            else:
                answer.append(candles[posj][1] - candles[posi][1])

        return answer


solution = Solution()

assert solution.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]) == [2, 3]

assert solution.platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]) == [9,0,0,0,0]
