'''
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
'''
from leetcode import *

# Time: O(n + m) where n is the length of arr and m is the number of queries.
# Space: O(n) where n is the length of arr. The output array is not counted because any solution would need to allocate space for the actual answer.
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorArr = [arr[0]]
        for i in range(1, len(arr)):
            xorArr.append(arr[i] ^ xorArr[i - 1])

        answers = [0]*len(queries)
        for i in range(len(queries)):
            left, right = queries[i]
            if (left - 1) < 0:
                answers[i] = xorArr[right]
            else:
                answers[i] = xorArr[right] ^ xorArr[left - 1]
        return answers

solution = Solution()

# Expected: [2,7,14,8]
print(solution.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))

# Expected: [8,0,4,4]
print(solution.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))
