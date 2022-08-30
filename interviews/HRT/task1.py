# Time complexity: O(n * log(m)) where n is the length of array X,
# and m is the max range of the integers in X/Y.
# Space complexity: O(n) where n is the length of array X.
def solution(X, Y):
    # Hash map of fractions to their counts.
    fractions = {}
    for i in range(len(X)):
        if X[i] == 0:
            fractions[X[i]] = fractions.setdefault(X[i], 0) + 1
        else:
            # Calculate the greatest common denominator
            # in order to reduce the fraction.
            factor = gcd(X[i], Y[i])
            fraction = (X[i] // factor, Y[i] // factor)
            fractions[fraction] = fractions.setdefault(fraction, 0) + 1

    # Find the fraction with the greatest count and return it.
    return max(fractions.values())


# Iterative implementation of Euclid's algorithm.
def gcd(a, b):
    while a != 0:
        b, a = a, b % a
    return b
