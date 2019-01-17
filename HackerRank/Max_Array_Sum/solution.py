"""
Input: an array of integers (1 <= n <= 10^5)
Output: the maximum sum of all the possible subsets of non-adjacent elements
This algorithm obviously runs in O(n) time using dynamic programming.
"""
def maxSubsetSum(a):
    n = len(a)
    if n < 1 or n > int(1e5):
        return None
    
    # recursion relation: s_n = max(s_(n-1), s_(n-2) + a[n])
    result_arr = [0, max(0, a[0])]
    for i in range(1, n):
        result_arr.append(max(result_arr[i], result_arr[i-1] + a[i]))

    return result_arr[n]
    
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(maxSubsetSum(a))

if __name__ == '__main__':
    main()
