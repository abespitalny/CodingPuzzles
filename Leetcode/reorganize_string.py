'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
'''
from leetcode import *

class Solution:
    # Time: O(n) Get counts in O(n), heapify, pop, and push into a heap of constant size given all inputs is constant time.
    # Space: O(1) excluding the output the heap and hashtable are limited by a constant which is the number of letters in the alphabet.
    # My solution is a little different than others because I take the most common element and keep using it while getting the most common next element.
    # Others are just using the two most common elements at every given stage, so there's only one while loop for the heap and not a nested pair.
    def reorganizeString(self, s: str) -> str:
        if len(s) <= 1:
            return s

        counts = {}
        for i in s:
            counts[i] = counts.setdefault(i, 0) + 1
        
        heap = [(-val, key) for key, val in counts.items()]
        heapq.heapify(heap)
        if -heap[0][0] == 1:
            return s

        ans = ""
        while len(heap) != 0:
            count, char = heapq.heappop(heap)
            count = -count
            if count == 1:
                ans += char
                continue

            while count > 1 and len(heap) != 0:
                nextCount, nextChar = heapq.heappop(heap)
                ans += (char + nextChar)
                count -= 1

                if (nextCount + 1) < 0:
                    heapq.heappush(heap, (nextCount + 1, nextChar))

            if count > 1:
                return ""
            ans += char
        return ans

solution = Solution()

# Expected: "aba"
print(solution.reorganizeString("aab"))

# Expected: ""
print(solution.reorganizeString("aaab"))
