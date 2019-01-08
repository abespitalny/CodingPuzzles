# Input:
# n: the number of socks in the pile (1 <= n <= 100)
# arr: the colors of each sock (1 <= arr[i] <= 100)
# Output: total number of matching pairs of socks (returns None if the input is invalid)
# Algorithm runs in O(n) time by using a hash table to store the occurrence of each sock
def sockMerchant(n, arr):
    if n < 1 or n > 100:
        return None
    
    hash_table = {}
    for i in arr:
        if i < 1 or i > 100:
            return None
        
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    pairs = 0
    # iterate through the keys; could be at most n of them
    for i in hash_table:
        # integer division to get the number of pairs from the count
        pairs += (hash_table[i] // 2)

    return pairs


def main():
    n = int(input())
    socks = list(map(int, input().split(" ")))
    print(sockMerchant(n, socks))

if __name__ == '__main__':
    main()
