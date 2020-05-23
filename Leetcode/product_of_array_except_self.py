'''
Given an array nums of n integers where n > 1, return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''
from leetcode import *

# This solution runs in O(n) time and uses O(1) space without performing division.
def product_except_self(nums: List[int]) -> List[int]:
    nums_size = len(nums)
    # Calculate the product going backward and store it in the output array
    # in order to not use any unnecessary space.
    output = [nums[-1]] * nums_size
    for i in range(nums_size - 2, -1, -1):
        output[i] = nums[i] * output[i + 1]

    # Use the original nums array to calculate the product going forward:
    for i in range(1, nums_size):
        nums[i] *= nums[i - 1]

    output[0] = output[1]
    for i in range(1, nums_size - 1):
        output[i] = nums[i - 1] * output[i + 1]
    output[-1] = nums[-2]
    return output


print(product_except_self([1, 2, 3, 4]))
