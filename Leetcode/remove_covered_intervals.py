'''
Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

Assume there is at least one interval given.
'''
from leetcode import *

# Time: O(n*log(n))
def remove_covered_intervals(intervals: List[List[int]]) -> int:
    # sort by the start ascending and then by the end descending
    intervals.sort(key=lambda x: (x[0], -x[1]))

    num_uncovered_intervals = 1
    prev_uncovered_interval_ind = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] == intervals[prev_uncovered_interval_ind][0]:
            continue
        elif (intervals[i][0] >= intervals[prev_uncovered_interval_ind][0]) and (intervals[i][1] <= intervals[prev_uncovered_interval_ind][1]):
            continue

        prev_uncovered_interval_ind = i
        num_uncovered_intervals += 1

    return num_uncovered_intervals

# Expected: 2
print(remove_covered_intervals([[1,4],[3,6],[2,8]]))
# Expected: 1
print(remove_covered_intervals([[1,4],[2,3]]))
# Expected: 2
print(remove_covered_intervals([[0,10],[5,12]]))
# Expected: 2
print(remove_covered_intervals([[3,10],[4,10],[5,11]]))
# Expected: 1
print(remove_covered_intervals([[1,2],[1,4],[3,4]]))
