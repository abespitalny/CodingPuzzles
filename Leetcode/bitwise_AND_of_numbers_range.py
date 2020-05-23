'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
'''
from leetcode import *

# Time: O(log(n)) where n is the number of bits since we have to shift log base 2 of n, Space: O(1).
def range_bitwise_and(m: int, n: int) -> int:
    ans = 0
    bit = 1 << 30
    while bit > 0:
        m_bit = m & bit
        n_bit = n & bit
        if m_bit == n_bit:
            ans |= m_bit
            bit >>= 1
        else:
            break
    return ans

# A clever O(1) time solution from Leetcode:
# Note: the key is taking the log base 2 of the range.
def range_bitwise_and_v2(m: int, n: int) -> int:
    diff = n - m
    if diff == 0:
        return n

    s = int(math.log(diff, 2))
    s += 1
    m &= n
    m >>= s
    m <<= s
    return m


# Expected: 4
print(range_bitwise_and(5, 7))
# Expected: 0
print(range_bitwise_and(0, 1))

print(range_bitwise_and_v2(5, 7))
print(range_bitwise_and_v2(0, 1))
# Expected: 5
print(range_bitwise_and_v2(5, 5))
