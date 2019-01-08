# A valley is a sequence of consecutive steps below sea-level,
# starting with a step down from sea-level and ending with a step up to sea-level.

# Input:
# n: the number of steps taken (2 <= n <= 10^6)
# s: a string describing the path (s[i] in {U, D})
# Output:
# a single integer that denotes the number of valleys walked through during the walk
def countingValleys(n, s):
    if n < 2 or n > 1000000:
        return None

    height = 0
    valleys = 0
    for i in s:
        if i == 'U':
            height += 1
        elif i == 'D':
            if height == 0:
                valleys += 1
            
            height -= 1
        else:
            return None

    return valleys if (height == 0) else None


def main():
    n = int(input())
    s = input()
    print(countingValleys(n, s))
    
if __name__ == '__main__':
    main()
