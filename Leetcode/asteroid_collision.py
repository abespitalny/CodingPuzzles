'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
'''
from leetcode import *

# Time: O(n), Space: O(n)
def asteroid_collision(asteroids: List[int]) -> List[int]:
    remaining_asteroids = [asteroids[0]]
    for i in range(1, len(asteroids)):
        asteroid = asteroids[i]
        if len(remaining_asteroids) > 0 and asteroid < 0:
            destroyed = False
            while len(remaining_asteroids) > 0:
                last_rem_asteroid = remaining_asteroids[-1]
                if last_rem_asteroid < 0:
                    break
                if last_rem_asteroid > abs(asteroid):
                    destroyed = True
                    break
                if last_rem_asteroid == abs(asteroid):
                    destroyed = True
                    remaining_asteroids.pop()
                    break
                remaining_asteroids.pop()

            if not(destroyed):
                remaining_asteroids.append(asteroid)
        else:
            remaining_asteroids.append(asteroids[i])

    return remaining_asteroids

# Expected: [5, 10]
print(asteroid_collision([5, 10, -5]))
# Expected: []
print(asteroid_collision([8, -8]))
# Expected: [10]
print(asteroid_collision([10, 2, -5]))
# Expected: [-2, -1, 1, 2]
print(asteroid_collision([-2, -1, 1, 2]))
