'''
The Tribonacci sequence Tn is defined as follows:
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

class Solution:
    # Bottom-up DP approach.
    # Time: O(n)
    # Space: O(1)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        t_n0 = 0
        t_n1 = t_n2 = 1

        for i in range(3, n + 1):
            t_n3 = t_n0 + t_n1 + t_n2
            t_n0 = t_n1
            t_n1 = t_n2
            t_n2 = t_n3
        
        return t_n2
