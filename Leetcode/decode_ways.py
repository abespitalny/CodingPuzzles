class Solution:
    # Bottom-up DP approach
    # Time: O(n) where n is the length of s
    # Space: O(n)
    def numDecodings(self, s: str) -> int:
        validEncodings = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19',
                          '20', '21', '22', '23', '24', '25', '26'}
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        if s[0] == '0':
            return 0
        dp[1] = 1

        for i in range(1, len(s)):
            numDecodings = 0
            if s[i] in validEncodings:
                numDecodings += dp[i]
            if s[(i - 1):(i + 1)] in validEncodings:
                numDecodings += dp[i - 1]

            dp[i + 1] = numDecodings
        return dp[-1]

    # Optimized bottom-up DP approach
    # Time: O(n) where n is the length of s
    # Space: O(n)
    def numDecodings2(self, s: str) -> int:
        if s[0] == '0':
            return 0

        validEncodings = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                          '11', '12', '13', '14', '15', '16', '17', '18', '19',
                          '20', '21', '22', '23', '24', '25', '26'}
        oneBack = 1
        twoBack = 1

        for i in range(1, len(s)):
            numDecodings = 0
            if s[i] in validEncodings:
                numDecodings += oneBack
            if s[(i - 1):(i + 1)] in validEncodings:
                numDecodings += twoBack

            oneBack, twoBack = numDecodings, oneBack
        return oneBack


solution = Solution()

assert solution.numDecodings("12") == 2
assert solution.numDecodings2("12") == 2

assert solution.numDecodings("226") == 3
assert solution.numDecodings2("226") == 3

assert solution.numDecodings("06") == 0
assert solution.numDecodings2("06") == 0
