'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'.
Each revision consists of digits and may contain leading zeros.
Every revision contains at least one character.
Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on.
For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order.
Revisions are compared using their integer value ignoring any leading zeros.
This means that revisions 1 and 001 are considered equal.
If a version number does not specify a revision at an index, then treat the revision as 0.
For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:
    - If version1 < version2, return -1.
    - If version1 > version2, return 1.
    - Otherwise, return 0.
'''
from leetcode import *

# Time: O(n), Space: O(n). One can easily write up a solution with O(1) additional space.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        subversions1 = version1.split('.')
        subversions2 = version2.split('.')
        
        for i in range(max(len(subversions1), len(subversions2))):
            v1 = 0 if i >= len(subversions1) else int(subversions1[i])
            v2 = 0 if i >= len(subversions2) else int(subversions2[i])
            
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
        return 0

solution = Solution()

# Expected: 0
print(solution.compareVersion("1.01", "1.001"))

# Expected: 0
print(solution.compareVersion("1.0", "1.0.0"))

# Expected: -1
print(solution.compareVersion("0.1", "1.1"))
