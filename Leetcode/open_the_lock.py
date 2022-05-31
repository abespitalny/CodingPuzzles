'''
You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''
from leetcode import *

class Solution:
    # Time: O(n^2 * 10**n + D) where n is the number of wheels in the lock and D is the number of combos in deadends.
    # Space: O(10**n + D) where n is the number of wheels in the lock and D is the number of combos in deadends.
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendsSet = set(deadends)
        startCombo = '0000'
        if startCombo in deadendsSet:
            return -1
        
        visited = set([startCombo])
        queue = deque([startCombo])
        turns = 0
        while len(queue) != 0:
            length = len(queue)
            for i in range(length):
                combo = queue.popleft()
                
                if combo == target:
                    return turns
                
                combo = list(combo)
                for i in range(len(combo)):
                    wheel = int(combo[i])

                    for j in range(2):
                        combo[i] = str((wheel + (-1)**j) % 10)
                        nextCombo = ''.join(combo)

                        if nextCombo in visited or nextCombo in deadendsSet:
                            continue

                        visited.add(nextCombo)
                        queue.append(nextCombo)

                    combo[i] = str(wheel)

            turns += 1
        
        return -1

solution = Solution()

# Expected: 6
print(solution.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))

# Expected: 1
print(solution.openLock(deadends = ["8888"], target = "0009"))

# Expected: -1
print(solution.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
