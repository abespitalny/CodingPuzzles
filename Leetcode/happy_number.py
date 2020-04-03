# Remember previously determined happy numbers:
num_happiness = {1: True}

# Assuming n is a positive integer
def isHappy(n: int) -> bool:
    happy_seq = set()
    next_num = n
    is_happy = None
    # set lookup is average O(1) while worst case is O(n)
    while next_num not in happy_seq:
        is_happy = num_happiness.get(next_num, None)
        if is_happy is not None:
            break
        happy_seq.add(next_num)
        next_num_sum = 0
        while next_num != 0:
            next_num_sum += (next_num % 10)**2
            next_num //= 10
        next_num = next_num_sum
    if is_happy is None:
        is_happy = False
    for i in happy_seq:
        num_happiness[i] = is_happy
    return is_happy

print(isHappy(19))
print(isHappy(1))
print(isHappy(0))
print(isHappy(2))
