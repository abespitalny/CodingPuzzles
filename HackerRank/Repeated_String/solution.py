# Input:
# s: a string to repeat (1 <= |s| <= 100)
# n: the number of chars to consider (1 <= n <= 10^12)
# Output: an integer denoting the number of letter a's in the first
# n letters of the infinite string created by repeating s infinitely many times
# Algorithm runs in O(1) time
def repeatedString(s, n):
    size = len(s)
    if size < 1 or size > 100 or n < 1 or n > int(1e12):
        return None
    
    return ((n // size) * s.count("a")) + s.count("a", 0, n % size)

def main():
    s = input()
    n = int(input())
    print(repeatedString(s, n))

if __name__ == '__main__':
    main()
