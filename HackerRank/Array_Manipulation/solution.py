"""
Input:
n: the number of elements in the array (3 <= n <= 10^7)
queries: a 2-D array of queries where each row contains three integers: a, b, and k
[a is the left index, b is the right index (inclusive), and k is the increment]
(1 <= m <= 2*10^5)
Output: the maximum value in the resulting array
"""
def arrayManipulation(n, queries):
    m = len(queries)
    if n < 3 or n > int(1e7) or m < 1 or m > int(2e5):
        return None

    # I will use a red-black tree in order to get the array operations down to
    # O(log(n)) so that the total runtime is O(m*log(n)).
    # Each node will store the max index of its range together with the value
    # stored in the array in that range
    

def main():
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])

    queries = []
    for i in range(m):
        queries.append(list(map(int, input().split(" "))))

    print(arrayManipulation(n, queries))

if __name__ == '__main__':
    main()
