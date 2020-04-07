'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''
# This algorithm runs in O(n) time.
# numRows is assumed to be > 0
def convert(s: str, numRows: int) -> str:
    s_len = len(s)
    if numRows <= 1 or numRows >= s_len:
        return s

    row_nums = [0] * s_len
    # Assign the row number to each char. Also, there must be at least 2 rows.
    row_num = 1
    
    diag_start_ind = numRows - 2
    # Is there a diagonal in the zig-zag pattern?
    if diag_start_ind > 0:
        # Are we currently not on a diagonal?
        off_diag = True
        for i in range(1, s_len):
            row_nums[i] = row_num
            if off_diag:
                row_num += 1
                if row_num == numRows:
                    row_num = diag_start_ind
                    off_diag = False
            else:
                row_num -= 1
                if row_num == 0:
                    off_diag = True
    else:
        for i in range(1, s_len):
            row_nums[i] = row_num
            row_num += 1
            if row_num == numRows:
                row_num = 0

    converted_s = [[] for i in range(numRows)]
    for i in range(s_len):
        converted_s[row_nums[i]].append(s[i])
    converted_s = ''.join(j for i in converted_s for j in i)
    return converted_s

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("AB", 1))
