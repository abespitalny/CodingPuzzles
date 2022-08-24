'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    - Every adjacent pair of words differs by a single letter.
    - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    - sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence
from beginWord to endWord, or 0 if no such sequence exists.
'''
from leetcode import *

class Solution:
    # BFS approach without optimization
    # Time: O(n*(m*n)) where m is the length of words and n is the number of words in word list
    # Space: O(m*n)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        minTransforms = 1
        queue = [beginWord]
        while len(queue) != 0:
            nextQueue = []
            for wordi in queue:
                if wordi == endWord:
                    return minTransforms

                words = []
                for wordj in wordSet:
                    numDiffs = 0
                    for ch1, ch2 in zip(wordi, wordj):
                        if ch1 != ch2:
                            numDiffs += 1
                    
                    if numDiffs == 1:
                        words.append(wordj)

                for wordj in words:
                    nextQueue.append(wordj)
                    wordSet.remove(wordj)

            queue = nextQueue
            minTransforms += 1

        return 0

    # BFS with optimization
    # Time: O(m*n + n*m) = O(m*n) where m is the length of the words and n is the number of words in word list.
    # Space: O(m*(m*n) + m*n + m*n) = O(m*(m*n)). This could be optimized further by using indices instead of duplicating the storage for the word.
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        wordToGeneric = {word: [] for word in wordList}

        if endWord not in wordToGeneric:
            return 0

        genericToWord = {}
        for i in range(len(wordList)):
            word = list(wordList[i])

            for j in range(len(beginWord)):
                temp = word[j]
                word[j] = '*'
                generic = ''.join(word)

                wordToGeneric[wordList[i]].append(generic)
                words = genericToWord.get(generic, set())
                words.add(wordList[i])
                genericToWord[generic] = words

                word[j] = temp

        minTransforms = 1
        visited = set([beginWord])
        queue = [beginWord]
        while len(queue) != 0:
            nextQueue = []
            for wordi in queue:
                if wordi == endWord:
                    return minTransforms

                for generic in wordToGeneric[wordi]:
                    for wordj in genericToWord[generic]:
                        if wordj not in visited:
                            nextQueue.append(wordj)
                            visited.add(wordj)

            queue = nextQueue
            minTransforms += 1

        return 0

    # The above approach can be further optimized by using bidirectional BFS. Basically, we start BFS from the beginWord and endWord
    # and terminate if we've reached a node in the middle that's already been visited by the other search.

solution = Solution()

assert solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5
assert solution.ladderLength2(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5

assert solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]) == 0
assert solution.ladderLength2(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5
