'''
Same description as word_ladder.py except:

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences
from beginWord to endWord, or an empty list if no such sequence exists.

Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
'''
from leetcode import *

class Solution:
    # Time: O(m*n + m*n + A) where m is the length of words, n is the number of words in list, and A is the number of shortest transformations.
    # Space: O(m*(m*n) + m*n + n) [basically, hash tables + visited/queue sets + backtracking stack] = O(m*(m*n)).
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        wordToGeneric = {word: [] for word in wordList}

        if endWord not in wordToGeneric:
            return []

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

        visited = {beginWord: None}
        queue = {beginWord}
        while len(queue) != 0:
            nextQueue = set()
            for wordi in queue:
                if wordi == endWord:
                    break

                for generic in wordToGeneric[wordi]:
                    for wordj in genericToWord[generic]:
                        if wordj not in visited:
                            nextQueue.add(wordj)
                            visited[wordj] = {wordi}
                        elif wordj in nextQueue and wordi not in visited[wordj]:
                            visited[wordj].add(wordi)

            queue = nextQueue


        ladders = []
        def dfs(startWord, path):
            path.append(startWord)

            if visited[startWord] is None:
                ladders.append(list(reversed(path)))
            else:
                for word in visited[startWord]:
                    dfs(word, path)

            path.pop()
            return

        if endWord not in visited:
            return ladders

        dfs(endWord, [])
        return ladders

solution = Solution()

# Expected: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
print(solution.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))

# Expected: []
print(solution.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
