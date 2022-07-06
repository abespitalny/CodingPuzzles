from leetcode import *

class Solution:
    # Hashmap approach
    # Time: O(n*m) where n is the number of domains and m is the maximum length of a domain.
    # Space: O(n*m) for storing the hashmap.
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        countPairSubdomains = {}
        for i in range(len(cpdomains)):
            rep, domain = cpdomains[i].split(' ')
            rep = int(rep)
            domain = domain.split('.')
            subdomain = ()
            
            for j in reversed(range(len(domain))):
                subdomain = (domain[j],) + subdomain
                countPairSubdomains.setdefault(subdomain, 0)
                countPairSubdomains[subdomain] += rep
        
        ans = []
        for subdomain, rep in countPairSubdomains.items():
            ans.append(f"{rep} {'.'.join(subdomain)}")
        return ans

solution = Solution()

# Expected: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
print(solution.subdomainVisits(["9001 discuss.leetcode.com"]))

# Expected: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
print(solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
