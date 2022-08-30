def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            # tmp = count[A[i]]
            tmp = count[A[i]] + 1
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            # count[A[i]] = tmp + 1
            count[A[i]] = tmp
        else:
            count[A[i]] = 1
    return A[index]

print(solution(3, [1, 2, 3, 3, 1, 3, 1]))
print(solution(10000, [1, 2, 3, 4, 10, 16, 10000]))
print(solution(1, [0]))
print(solution(5, [1, 4, 2, 3, 4]))
