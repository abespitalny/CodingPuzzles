'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
'''
from leetcode import *

class TrieNode:
    def __init__(self):
        # An index to not just mark that this is a word but what word in a list of words is it.
        self.wordEnd = -1
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(m*n) where m is max length of a word in words and n is the number of words.
    # Space: O(m*n) because we might need to insert new nodes for each word.
    def insertWords(self, words: List[str]) -> None:        
        self.words = words

        for i in range(len(words)):
            node = self.root
            for j in words[i]:            
                nextNode = node.children.get(j, None)
                if nextNode != None:
                    node = nextNode
                else:
                    newNode = TrieNode()
                    node.children[j] = newNode
                    node = newNode
            node.wordEnd = i
        return

    # Time: O(m) where m is the length of the word.
    # Space: O(m) because of the path array.
    def deleteWord(self, word: str) -> None:
        node = self.root
        path = [node]
        for i in word:
            node = node.children[i]
            path.append(node)

        path[-1].wordEnd = -1
        # There are words below this one, so don't delete anything.
        if len(path[-1].children) != 0:
            return

        i = len(path) - 1
        while i > 0 and len(path[i].children) < 2 and path[i].wordEnd == -1:
            i -= 1
        del path[i].children[word[i]]
        return

    # Backtracking approach with trie.
    # Time: O(m*n*3^L) where the board is an m x n matrix and L is the maximum length of a word.
    # Space: O(L + L*k) where L is the maximum length of a word and k is the number of words to find
    # because of the recursive stack and the set of seen positions as well as maintaining the trie.
    def findWords(self, board: List[List[str]]) -> List[str]:
        m = len(board)
        n = len(board[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        wordsFound = []

        def backtrack(i, j, node, seen):
            seen.add((i, j))
            node = node.children[board[i][j]]

            if node.wordEnd >= 0:
                wordsFound.append(self.words[node.wordEnd])
                # Delete the word from the trie once it was found.
                self.deleteWord(self.words[node.wordEnd])

            for x, y in directions:
                x += i
                y += j

                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in seen or board[x][y] not in node.children:
                    continue

                backtrack(x, y, node, seen)
                seen.remove((x, y))
            return

        seen = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.root.children:
                    backtrack(i, j, self.root, seen)
                    seen.remove((i, j))
        return wordsFound

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        trie.insertWords(words)

        return trie.findWords(board)


solution = Solution()

# Expected: ["eat","oath"]
print(solution.findWords(board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words=["oath","pea","eat","rain"]))

# Expected: []
print(solution.findWords(board=[["a","b"],["c","d"]], words=["abcb"]))
