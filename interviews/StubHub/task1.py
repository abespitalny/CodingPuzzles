# Time Complexity: O(6^F)
# Space Complexity: O(F)
def solution(A, F, M):
    sumF = (M * (len(A) + F)) - sum(A)
    MAX_VAL = 6
    
    if (sumF < 1) or (MAX_VAL*F < sumF):
        return [0]
  
    def backtrack(target, rolls):
        nonlocal possibleRolls
        if target == 0 and len(rolls) == F:
            possibleRolls = rolls
            return True
        elif target < 0 or len(rolls) >= F:
            return False
        
        for i in range(1, MAX_VAL + 1):
            rolls.append(i)
            if backtrack(target - i, rolls):
                return True
            rolls.pop()
        return False
    
    possibleRolls = [0]
    backtrack(sumF, [])
    return possibleRolls

print(solution([2, 3, 5], 4, 3))

# Aaron's idea
# Time: O(F)
# Space: O(1) if we exclude output
def solution2(A, F, M):
    sumF = (M * (len(A) + F)) - sum(A)
    MIN_VAL = 1
    MAX_VAL = 6

    if (sumF < MIN_VAL*F) or (MAX_VAL*F < sumF):
        return [0]

    rolls = [1]*F
    sumF -= MIN_VAL*F
    i = 0
    while sumF > 0:
        inc = min(sumF, MAX_VAL - MIN_VAL)
        rolls[i] += inc
        sumF -= inc
        i += 1

    return rolls

print(solution2([2, 3, 5], 4, 3))
print(solution2([4,5,6,2,1,1,3,5,3,4,1,2,3,5,4,6], 99999, 5))
