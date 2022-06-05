'''
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
'''

class Solution:
    # Recursive approach
    # Time: O(n)
    # Space: O(n)
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        isKEven = (k % 2 == 0)
        if isKEven:
            prevK = k // 2
        else:
            prevK = (k + 1) // 2

        symbol = self.kthGrammar(n - 1, prevK)
        
        if isKEven:
            return 1 if symbol == 0 else 0
        else:
            return 0 if symbol == 0 else 1

solution = Solution()

# Expected: 0
print(solution.kthGrammar(n = 1, k = 1))

# Expected: 0
print(solution.kthGrammar(n = 2, k = 1))

# Expected: 1
print(solution.kthGrammar(n = 2, k = 2))
