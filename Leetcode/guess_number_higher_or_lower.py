'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
    -1: Your guess is higher than the number I picked (i.e. num > pick).
     1: Your guess is lower than the number I picked (i.e. num < pick).
     0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.
'''

pick = 6
def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    return 0

class Solution:
    # Binary search approach
    # Time: O(log(n))
    # Space: O(1)
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            outcome = guess(mid)
            
            if outcome == -1:
                right = mid - 1
            elif outcome == 1:
                left = mid + 1
            else:
                return mid
        return -1
