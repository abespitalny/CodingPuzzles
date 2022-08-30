# Time complexity: O(len(S))
# Space complexity: O(1)
def solution(S):
    # Strip leading zeros
    i = 0
    while i < len(S) and S[i] == "0":
        i += 1
    
    # S is just a string of 0s.
    if i == len(S):
        return 0

    msb = i
    lsb = len(S) - 1
    numOps = 0
    while lsb > msb:
        # Need to perform subtract by 1 operation if S is odd.
        if S[lsb] == "1":
            numOps += 1
        # Need to perform divide by 2 operation if S is even, S >> 1.
        lsb -= 1
        numOps += 1
    
    # Last digit is "1"
    return numOps + 1

assert solution("011100") == 7
assert solution("111") == 5
assert solution("1111010101111") == 22
assert solution("1"*400_000) == 799_999
