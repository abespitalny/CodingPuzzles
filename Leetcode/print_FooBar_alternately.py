from leetcode import *

class FooBar:
    def __init__(self, n):
        self.n = n
        self.cv = threading.Condition(threading.Lock())
        # Whose turn is it to go?
        self.foo_turn = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        cv = self.cv
        for i in range(self.n):
            with cv:
                while not(self.foo_turn):
                    cv.wait()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.foo_turn = False
                cv.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        cv = self.cv
        for i in range(self.n):
            with cv:
                while self.foo_turn:
                    cv.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.foo_turn = True
                cv.notify()

def printFoo() -> None:
    print('foo', end='')

def printBar() -> None:
    print('bar', end='')

n = 10
foobar = FooBar(n)
thread_a = threading.Thread(target=foobar.foo, args=(printFoo,))
thread_b = threading.Thread(target=foobar.bar, args=(printBar,))

thread_a.start()
thread_b.start()

# An alternate solution from LeetCode that was smart:

# class FooBar:
#     def __init__(self, n):
#         self.n = n
#         self.b = threading.Lock()
#         self.a = threading.Lock()
#         self.b.acquire()

#     def foo(self, printFoo: 'Callable[[], None]') -> None:        
#         for i in range(self.n):
#             self.a.acquire()
#             # printFoo() outputs "foo". Do not change or remove this line.
#             printFoo()
#             self.b.release()

#     def bar(self, printBar: 'Callable[[], None]') -> None:        
#         for i in range(self.n):
#             self.b.acquire()
#             # printBar() outputs "bar". Do not change or remove this line.
#             printBar()
#             self.a.release()
