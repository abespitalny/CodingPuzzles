"""
Input: an array of integers (1 <= n <= 10^5 and -10^4 <= a[i] <= 10^4)
Output: the maximum sum of all the possible subsets of non-adjacent elements
"""
def maxSubsetSum(a):
    n = len(a)
    if n < 1 or n > 100000:
        return None

    
    
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(maxSubsetSum(a))

if __name__ == '__main__':
    main()
