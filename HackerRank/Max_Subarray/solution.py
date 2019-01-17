import sys

'''
Input: an array of integers (1 <= n <= 10^5)
Output: array of two integers, the max subarray sum and the max subsequence sum
of the input array (note: subarray or subsequence cannot be empty).
This algorithm runs in O(n) time, and not only finds the sum of the max subsequence
and subarray but also finds the elements in them.
'''
def maxSubarray(a):
    n = len(a)
    if n < 1 or n > int(1e5):
        return None

    max_elem_ind = 0
    sub_arr_sum, max_sub_arr_sum, sub_seq_sum = 0, 0, 0
    left, max_left, max_right = 0, -1, -1
    seq = []
    for i in range(0, n):
        if a[i] > a[max_elem_ind]:
            max_elem_ind = i
        # calculate max subsequence
        if a[i] > 0:
            sub_seq_sum += a[i]
            seq.append(a[i])
        
        if (sub_arr_sum + a[i]) <= 0:
            left = i + 1
            sub_arr_sum = 0
        elif (sub_arr_sum + a[i]) > 0:
            sub_arr_sum += a[i]
            if sub_arr_sum > max_sub_arr_sum:
                max_left = left
                max_right = i + 1
                max_sub_arr_sum = sub_arr_sum
    # this could happen if all the elements of the input array are negative
    if len(seq) == 0:
        max_elem = a[max_elem_ind]
        seq.append(max_elem)
        sub_seq_sum = max_elem
        max_sub_arr_sum = max_elem
        max_left = max_elem_ind
        max_right = max_elem_ind + 1

    # print max subsequence and subarray to stderr
    print("Max subarray:", a[max_left:max_right], file=sys.stderr)
    print("Max subsequence:", seq, file=sys.stderr)

    return [max_sub_arr_sum, sub_seq_sum]

