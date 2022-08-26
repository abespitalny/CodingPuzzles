'''
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:
    - If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    - Otherwise, it becomes vacant.

Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant,
and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).
'''
from leetcode import *

class Solution:
    # Simulation with fast-forwarding
    # Time: O(k*min(n, 2^k)) where k is the number of cells evolving (here it's 6)
    # Space: O(2^k)
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        states = set()
        sequence = []
        numCells = 6
        nextState = [0]*len(cells)

        numStates = 2**numCells
        for i in range(min(n, numStates)):
            stateNum = 0
            nextState[0] = 0
            nextState[-1] = 0
            for i in range(1, numCells + 1):
                nextState[i] = 1 if (cells[i - 1] == cells[i + 1]) else 0
                stateNum = (stateNum << 1) + nextState[i]

            cells, nextState = nextState, cells

            if stateNum in states:
                break
            else:
                states.add(stateNum)
                sequence.append(stateNum)

        finalState = sequence[(n - 1) % len(sequence)]
        for i in range(numCells, 0, -1):
            cells[i] = (finalState & 1)
            finalState >>= 1
        return cells

solution = Solution()

assert solution.prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], n = 7) == [0,0,1,1,0,0,0,0]
assert solution.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 1000000000) == [0,0,1,1,1,1,1,0]
