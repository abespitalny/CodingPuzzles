'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''

class Solution:
    # Backtrack approach
    # Time: O(n!). See the first N-Queens problem explanation.
    # Space: O(n) for the recursion stack and the sets for cols, hills, and dales.
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, hills, dales):
            if row == n:
                return 1
            
            count = 0
            for i in range(n):
                hill = row - i
                dale = row + i
                
                if i in cols or hill in hills or dale in dales:
                    continue
                
                cols.add(i)
                hills.add(hill)
                dales.add(dale)
                
                count += backtrack(row + 1, cols, hills, dales)
                
                cols.remove(i)
                hills.remove(hill)
                dales.remove(dale)

            return count

        return backtrack(0, set(), set(), set())

solution = Solution()

# Expected: 2
print(solution.totalNQueens(4))

# Expected: 1
print(solution.totalNQueens(1))
