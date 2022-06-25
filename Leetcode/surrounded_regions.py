'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
from leetcode import *

def solve(board: List[List[str]]) -> None:
    m = len(board)
    n = len(board[0])
    ovisited = set()
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] == 'X':
                continue
            # Else, it's an 'O':
            if (i, j) in ovisited:
                continue
        
            opath = set()
            ostack = [(i, j)]
            on_boundary = False
            while len(ostack) > 0:
                cur_pos = ostack.pop()
                opath.add(cur_pos)
                x, y = cur_pos
                if x == 0 or x == (m - 1) or y == 0 or y == (n - 1):
                    on_boundary = True

                left_pos = (0 if (x - 1) < 0 else (x - 1), y)
                top_pos = (x, 0 if (y - 1) < 0 else (y - 1))
                right_pos = ((m - 1) if (x + 1) == m else (x + 1), y)
                bottom_pos = (x, (n - 1) if (y + 1) == n else (y + 1))

                if left_pos not in opath and board[left_pos[0]][left_pos[1]] == 'O':
                    ostack.append(left_pos)
                if top_pos not in opath and board[top_pos[0]][top_pos[1]] == 'O':
                    ostack.append(top_pos)
                if right_pos not in opath and board[right_pos[0]][right_pos[1]] == 'O':
                    ostack.append(right_pos)
                if bottom_pos not in opath and board[bottom_pos[0]][bottom_pos[1]] == 'O':
                    ostack.append(bottom_pos)
            
            if on_boundary:
                for o in opath:
                    ovisited.add(o)
            else:
                for o in opath:
                    board[o[0]][o[1]] = 'X'

baord = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(baord)
print(baord)