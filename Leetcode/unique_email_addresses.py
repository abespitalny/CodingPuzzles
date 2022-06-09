from leetcode import *

class Solution:
    # Time: O(n*s) where n is the number of emails and s is the maximum length of an email.
    # Space: O(n*s)
    def numUniqueEmails(self, emails: List[str]) -> int:
        sent = set()
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            parsedLocal = []
            for j in local:
                if j == '.':
                    continue
                elif j == '+':
                    break
                else:
                    parsedLocal.append(j)
            
            parsedLocal = ''.join(parsedLocal)
            sent.add((parsedLocal, domain))

        return len(sent)

solution = Solution()

# Expected: 2
print(solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

# Expected: 3
print(solution.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
