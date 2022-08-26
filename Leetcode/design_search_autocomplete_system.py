'''
Design a search autocomplete system for a search engine.
Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n
where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed.
For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:
    - The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    - The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
      If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
    - If less than 3 hot sentences exist, return as many as you can.
    - When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Implement the AutocompleteSystem class:
    - AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
    - List<String> input(char c) This indicates that the user typed the character c.
        - Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
        - Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.
          If there are fewer than 3 matches, return them all.
'''
from leetcode import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.hot = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Time: O(n) where n is the length of sentence
    # Space: O(n^2) because we store the sentence and its count at every node
    def insert(self, sentence: str, times: int) -> None:
        node = self.root
        for c in sentence:
            if c not in node.children:
                newNode = TrieNode()
                node.children[c] = newNode

            node = node.children[c]
            node.hot[sentence] += times


class AutocompleteSystem:
    # Time: O(m*n) where m is the max length of a sentence and n is the number of sentences.
    # Space: O(m*(m*n))
    def __init__(self, sentences: List[str], times: List[int]):
        self.sentence = []
        self.trie = Trie()
        self.node = self.trie.root

        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])

    # Time: O(n*log(n)) where n is the number of sentences.
    # Space: O(n)
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(''.join(self.sentence), 1)
            self.sentence = []
            self.node = self.trie.root
            return []

        self.sentence.append(c)
        if self.node is None:
            return []
        if c not in self.node.children:
            self.node = None
            return []

        self.node = self.node.children[c]
        
        hot = list(self.node.hot.items())
        hot.sort(key=lambda x: (-x[1], x[0]))
        
        top3 = []
        for i in range(min(len(hot), 3)):
            top3.append(hot[i][0])
        return top3

obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])

assert obj.input("i") == ["i love you", "island", "i love leetcode"]
assert obj.input(" ") == ["i love you", "i love leetcode"]
assert obj.input("a") == []
assert obj.input("#") == []
