'''
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''
from leetcode import *

# Time: O(n*log(n)) because we sort the array first.
# Space: O(1) because we sort in-place.
# Note: without the constraint of 2 per boat, then we would have an NP-hard problem (https://en.wikipedia.org/wiki/Bin_packing_problem).
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        numBoats = 0
        start = 0
        end = len(people) - 1
        while start <= end:
            if (people[start] + people[end]) <= limit:
                start += 1
            end -= 1
            numBoats += 1
        return numBoats

solution = Solution()

# Expected: 1
print(solution.numRescueBoats(people = [1,2], limit = 3))

# Expected: 3
print(solution.numRescueBoats(people = [3,2,2,1], limit = 3))

# Expected: 4
print(solution.numRescueBoats(people = [3,5,3,4], limit = 5))
