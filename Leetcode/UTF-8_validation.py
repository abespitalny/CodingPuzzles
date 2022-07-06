'''
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
    1. For a 1-byte character, the first bit is a 0, followed by its Unicode code.
    2. For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.

This is how the UTF-8 encoding would work:
     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data.
This means each integer represents only 1 byte of data.
'''
from leetcode import *

class Solution:
    # Bit manipulation approach
    # Time: O(n) where n is the number of bytes in data.
    # Space: O(1)
    def validUtf8(self, data: List[int]) -> bool:
        mask = 0xFF
        firstBit = 0x80
        firstTwoBits = 0xC0
        octetSeqBits = 0x80
        
        i = 0
        while i < len(data):
            octet = data[i] & mask
            # 1 byte
            if octet & firstBit == 0:
                i += 1
            # multiple bytes
            else:
                numberOfOnes = 1
                bitMask = firstBit >> 1
                while (octet & bitMask) != 0:
                    numberOfOnes += 1
                    bitMask >>= 1

                if numberOfOnes == 1 or numberOfOnes > 4 or (i + numberOfOnes) > len(data):
                    return False
                
                for j in range(1, numberOfOnes):
                    nextOctet = data[i + j] & mask
                    if (nextOctet & firstTwoBits) != octetSeqBits:
                        return False
                i += numberOfOnes

        return True

solution = Solution()

assert solution.validUtf8([197,130,1]) == True
assert solution.validUtf8([235,140,4]) == False
