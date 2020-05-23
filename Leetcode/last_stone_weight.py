'''
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:
- If x == y, both stones are totally destroyed;
- If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''
from leetcode import *

def insert_binary_search(arr: List[int], new_val: int) -> None:
    start = 0
    end = len(arr)
    if start == end:
        arr.insert(start, new_val)
        return

    mid = (start + end) // 2
    while start < (end - 1):
        mid_val = arr[mid]
        if new_val == mid_val:
            arr.insert(mid, new_val)
            return
        elif new_val > mid_val:
            start = mid
        else:
            end = mid
        mid = (start + end) // 2

    if new_val > arr[mid]:
        arr.insert(end, new_val)
        return
    arr.insert(start, new_val)

# Note: 1 <= stones.length <= 30
# This is an O(n*log(n)) algorithm in time because of the sorting.
def last_stone_weight(stones: List[int]) -> int:
    if len(stones) == 1:
        return stones[0]

    # Sorting takes O(n*log(n)) (note: Python uses Timsort which has O(n*log(n)) as its worst-case):
    stones.sort()
    while len(stones) > 1:
        last = stones.pop()
        seclast = stones.pop()
        if last != seclast:
            remaining_weight = last - seclast
            # Insert the remaining weight back into the array in O(log(n)) time.
            insert_binary_search(stones, remaining_weight)
    return 0 if len(stones) == 0 else stones[0]


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
