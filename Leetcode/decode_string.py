'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
'''

class Solution:
    # Some help from Leetcode to interpret time complexity. Time: O((maxK^countK) * n) where maxK is the maximum k value in encoded string,
    # countK is the number of nested k values, and n is the length of the maximum encoded string.
    # Space: O(sum((maxK^countK) * n)).
    def decodeString(self, s: str) -> str:
        i = 0
        stack = []
        while i < len(s):
            k = ""
            while s[i].isdigit():
                k += s[i]
                i += 1

            if len(k) > 0:
                stack.append(k)

            if s[i] == ']':
                decodedStr = []
                while not(stack[-1].isdigit()):
                    decodedStr.append(stack.pop())

                decodedStr = int(stack.pop()) * ''.join(reversed(decodedStr))
                stack.append(decodedStr)

            elif s[i] != '[':
                stack.append(s[i])

            i += 1
        
        return ''.join(stack)
    
    # Other Leetcode solutions seemed more complex and none were in Python.

solution = Solution()

# Expected: "aaabcbc"
print(solution.decodeString("3[a]2[bc]"))

# Expected: "accaccacc"
print(solution.decodeString("3[a2[c]]"))

# Expected: "abcabccdcdcdef"
print(solution.decodeString("2[abc]3[cd]ef"))
