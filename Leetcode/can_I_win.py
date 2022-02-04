from leetcode import *

# I believe it's Time: O(2^n), Space: O(2^n) where n is maxChoosableInteger
# because we have to check each bitmap sequence of choosable integers. Top-down approaches usually look like this.
class Solution:
    def __init__(self):
        # The key is an integer representing a bitmap of choosable integers.
        # The value is whether the first player can force a win with that set of choosable integers.
        self.memo_table = None

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True

        self.memo_table = {}
        return self.canIWinRecurse(True, (2**maxChoosableInteger) - 1, maxChoosableInteger, desiredTotal)

    def canIWinRecurse(self, firstPlayer: bool, choosableIntegers: int, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if choosableIntegers in self.memo_table:
            return self.memo_table[choosableIntegers]

        wins = []
        for i in range(maxChoosableInteger):
            index = (1 << i)
            choosable = choosableIntegers & index
            if choosable:
                total = desiredTotal - (i + 1)
                if total <= 0:
                    wins.append(firstPlayer)
                    break

                integers = choosableIntegers & (~index)
                outcome = self.canIWinRecurse(not(firstPlayer), integers, maxChoosableInteger, total)
                wins.append(outcome)
                if outcome == firstPlayer:
                    break

        win = False
        if len(wins) > 0:
            # For first player, if one of the branches wins, then we can win.
            # For the second player, if all branches win, then first player wins.
            win = any(wins) if firstPlayer else all(wins)
        
        self.memo_table[choosableIntegers] = win
        return win

solution = Solution()

# Expected: False
print(solution.canIWin(10, 11))

# Expected: True
print(solution.canIWin(10, 0))

# Expected: True
print(solution.canIWin(10, 1))
