'''
You are controlling a robot that is located somewhere in a room.
The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid,
but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room).
The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.
'''

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    # Time: O(n) where n is the number of rooms to clean.
    # Space: O(n) because of the hashset.
    def cleanRoom(self, robot):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def backtrack(robot, pos, orient, cleanedRooms):
            robot.clean()
            cleanedRooms.add(pos)
            for i in range(4):
                robot.turnLeft()
                orient = (orient + 1) % 4
                newPos = (pos[0] + directions[orient][0], pos[1] + directions[orient][1])

                if newPos not in cleanedRooms and robot.move():
                    backtrack(robot, newPos, orient, cleanedRooms)

                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()                

            return

        backtrack(robot, (0, 0), 0, set())
