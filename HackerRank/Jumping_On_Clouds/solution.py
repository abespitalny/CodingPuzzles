# Input:
# c: an array of binary digits indicating if the cloud is a cumulus (0) or
# thunderhead (1)
# Output: the minimum number of jumps required (assuming a winning path is possible)
# Algorithm obviously runs in O(n) time
def jumpingOnClouds(c):
    n = len(c)
    # Valid input is if 2 <= n <= 100 and c[0] = c[n-1] = 0
    if n < 2 or n > 100 or c[0] != 0 or c[0] != c[n-1]:
        return None

    jumps = 0
    i = 0
    while i < (n-1):
        if (i + 2) < n and c[i+2] == 0:
            jumps += 1
            i += 2
        elif c[i+1] == 0:
            jumps += 1
            i += 1
        # Cannot jump so input must be invalid
        else:
            return None

    return jumps


def main():
    n = int(input())
    clouds = list(map(int, input().split(" ")))
    print(jumpingOnClouds(clouds))

if __name__ == '__main__':
    main()
