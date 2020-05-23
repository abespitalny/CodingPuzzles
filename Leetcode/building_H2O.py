'''
Input: "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.

Constraints:
- Total length of input string will be 3n, where 1 <= n <= 20.
- Total number of H will be 2n in the input string.
- Total number of O will be n in the input string.
'''
from leetcode import *

class H2O:
    def __init__(self):
        self.hlock = threading.Lock()
        self.olock = threading.Lock()
        self.h1 = True
        self.hlock.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.olock.acquire()
        if self.h1:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.h1 = False
            self.hlock.release()
        else:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.h1 = True
            self.olock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.hlock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.olock.release()


def releaseHydrogen() -> None:
    print('H', end='')

def releaseOxygen() -> None:
    print('O', end='')

molecules = 'OHOHOHOHHHHH'
h20 = H2O()
for m in molecules:
    if m == 'H':
        threading.Thread(target=h20.hydrogen, args=(releaseHydrogen,)).start()
    else:
        threading.Thread(target=h20.oxygen, args=(releaseOxygen,)).start()

# There was a bunch of other really smart solutions on LeetCode using semaphores, barriers, etc.