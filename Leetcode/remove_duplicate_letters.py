# Time: O(n) where n = len(s).
# Space: O(n). Each letter might be unique.
# From leetcode, space is O(1)! The number of unique letters is bounded by a constant, namely, the number of letters in the alphabet.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lettersToLastPosition = {}
        for i in range(len(s)):
            lettersToLastPosition[s[i]] = i
        
        stack = [s[0]]
        lettersInStack = set([s[0]])
        for i in range(1, len(s)):
            if s[i] in lettersInStack:
                continue

            while len(stack) != 0:
                top = stack[-1]
                if s[i] < top and lettersToLastPosition[top] > i:
                    stack.pop()
                    lettersInStack.remove(top)
                else:
                    break

            stack.append(s[i])
            lettersInStack.add(s[i])
        
        return ''.join(stack)

solution = Solution()

# Expected: abc
print(solution.removeDuplicateLetters("bcabc"))

# Expected: acdb
print(solution.removeDuplicateLetters("cbacdcbc"))
