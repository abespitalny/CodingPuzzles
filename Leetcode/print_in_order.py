'''
The same instance of Foo will be passed to three different threads.
Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(),
and thread C calls second(). "firstsecondthird" is the correct output.
'''
import threading

class Foo:
    def __init__(self):
        # Lock is, I think, more efficient than RLock.
        self.cv = threading.Condition(threading.Lock())
        self.counter = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        cv = self.cv
        with cv:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.counter += 1
            cv.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        cv = self.cv
        with cv:
            while self.counter != 2:
                cv.wait()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.counter += 1
            cv.notify()

    def third(self, printThird: 'Callable[[], None]') -> None:
        cv = self.cv
        with cv:
            while self.counter != 3:
                cv.wait()
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


def printFirst():
    print('first', end='')

def printSecond():
    print('second', end='')

def printThird():
    print('third')

foo = Foo()
func_thread_order = {1: [None, foo.first, printFirst], 2: [None, foo.second, printSecond], 3: [None, foo.third, printThird]}
for i in func_thread_order:
    func_thread_order[i][0] = threading.Thread(target=func_thread_order[i][1], args=(func_thread_order[i][2],))

for i in func_thread_order:
    func_thread_order[i][0].start()
