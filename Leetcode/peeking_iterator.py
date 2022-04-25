# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# Time: O(1) for all operations except initialization which is O(n).
# Space: O(n) because we allocate space for an array.
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.index = 0
        self.iterator = []
        while iterator.hasNext():
            self.iterator.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.iterator[self.index]

    def next(self):
        """
        :rtype: int
        """
        curIndex = self.index
        self.index += 1
        return self.iterator[curIndex]

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.index < len(self.iterator))

# A better solution inspired by Leetcode.
# Time: O(1) for all operations.
# Space: O(1).
class PeekingIterator2:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.curElem = iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.curElem

    def next(self):
        """
        :rtype: int
        """
        prevElem = self.curElem
        if self.iterator.hasNext():
            self.curElem = self.iterator.next()
        else:
            self.curElem = None
        return prevElem

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.curElem != None)
