from leetcode import *

# Time: O(n^2), Space: O(n) where n is query_row
def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    if poured == 0:
        return 0
    
    glasses = [poured]
    row = 0
    while row < query_row:
        next_row = [0]
        for i in range(len(glasses)):
            half_excess = max(0, glasses[i] - 1) / 2
            next_row[i] += half_excess
            next_row.append(half_excess)

        glasses = next_row
        row += 1

    if query_row > row:
        return 0

    wine_amount = (1 if glasses[query_glass] > 1 else glasses[query_glass])
    return wine_amount

# Expected: 0
print(champagne_tower(1, 1, 1))
# Expected: 0.5
print(champagne_tower(2, 1, 1))
# Expected: 1
print(champagne_tower(100000009, 33, 17))
# Expected: 0.125
print(champagne_tower(8, 3, 0))
