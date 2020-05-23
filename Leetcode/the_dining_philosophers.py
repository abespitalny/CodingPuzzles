'''
The philosophers' ids are numbered from 0 to 4 in a clockwise order.
The philosophers are assumed to be thinking as long as they are not asking to eat
(the function is not being called with their number). Five threads, each representing a philosopher,
will simultaneously use one object of your class to simulate the process.
The function may be called for the same philosopher more than once, even before the last call ends.
'''
from leetcode import *

class DiningPhilosophers:
    def __init__(self):
        self.lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        with self.lock:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()

# This is a very interesting general problem that should be explored further.
# My dead simple solution here does not give it justice.
