'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.
The robot can receive one of three instructions:
- "G": go straight 1 unit;
- "L": turn 90 degrees to the left;
- "R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''
# Time: O(n), since it requires only one iteration of the instructions. Space: O(1),
# since the only state saved is the angle and the position of the robot.
def is_robot_bounded(instructions: str) -> bool:
    # Facing north initially:
    angle = 0
    # At the center initially:
    pos = [0, 0]
    for i in range(len(instructions)):
        c = instructions[i]
        if c == "G":
            if angle == 0:
                pos[1] += 1
            elif angle == 90:
                pos[0] += 1
            elif angle == 180:
                pos[1] -= 1
            else:
                pos[0] -= 1
        elif c == "L":
            angle = (angle - 90) % 360
        else:
            angle = (angle + 90) % 360
    # It's not bounded in a circle if the robot faces in the same direction
    # and is displaced from the center after one iteration of the instructions.
    # The returned expression is the negation of the above statement since it needs to
    # return True when it is bounded.
    return (angle != 0) or (pos[0] == 0 and pos[1] == 0)

# Another interesting solution, but it is slower than mine, is to check if after 2 or 4 iterations
# of the instructions if the robot is back in the same place and direction that it started in. If so,
# the robot makes a line (for 2 iterations) or circle (for 4 iterations) forever, so it's bounded;
# else, it's not bounded.

# Expected: True
print(is_robot_bounded("GR"))
# Expected: True
print(is_robot_bounded("GRGRGRG"))
# Expected: True
print(is_robot_bounded("GRR"))
# Expected: False
print(is_robot_bounded("RRGRR"))
# Expected: False
print(is_robot_bounded("GRRGGLL"))
# Expected: True
print(is_robot_bounded("GRRGG"))
# Expected: False
print(is_robot_bounded("RGL"))
# Expected: True
print(is_robot_bounded("RGR"))
# Expected: False
print(is_robot_bounded("GRGLGLGRG"))
