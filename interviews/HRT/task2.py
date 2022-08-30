# Global variable to store the vowels.
vowels = ['a', 'e', 'i', 'o', 'u']

# Time complexity: O(n*log(n)) where n is the length of the string S.
# Space complexity: O(n) where n is the length of the string S.
def solution(S):
    N = len(S)
    # Base cases
    if N == 0:
        return 0
    elif N == 1:
        return 1

    numVowels = 0
    for i in S:
        if i in vowels:
            numVowels += 1
    
    numConsonants = N - numVowels

    return abs(numConsonants - numVowels) + solution(S[:N//2]) + solution(S[N//2:])


print(solution("sample"))

print(solution("leetcode"))

print(solution(""))

print(solution("le"))