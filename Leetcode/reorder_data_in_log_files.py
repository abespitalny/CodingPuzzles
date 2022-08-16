'''
You are given an array of logs.
Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:
    - Letter-logs: All words (except the identifier) consist of lowercase English letters.
    - Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
    - The letter-logs come before all digit-logs.
    - The letter-logs are sorted lexicographically by their contents.
      If their contents are the same, then sort them lexicographically by their identifiers.
    - The digit-logs maintain their relative ordering.

Return the final order of the logs.
'''
from leetcode import *

class Solution:
    # Time: O(L*len(L)*log(len(L)) + D) where L is the number of characters in letter-logs, len(L) is the number of letter-logs,
    # and D is the number of characters in digit-logs.
    # Space: O(L*len(L) + len(D))
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []

        for i in range(len(logs)):
            log = logs[i]
            identifier = []

            for j in range(len(log)):
                if log[j] == " ":
                    if log[j + 1].isdigit():
                        digitLogs.append(i)
                    else:
                        letterLogs.append((log[j + 1:], ''.join(identifier)))

                    break
                else:
                    identifier.append(log[j])

        letterLogs.sort()
        sortedLogs = []

        for content, identifier in letterLogs:
            sortedLogs.append(f"{identifier} {content}")

        for i in digitLogs:
            sortedLogs.append(logs[i])

        return sortedLogs

    # There are much more clever ways to solve this by using a comparator or sorting by keys. See Leetcode solution.

solution = Solution()

# Expected: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
print(solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

# Expected: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print(solution.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
