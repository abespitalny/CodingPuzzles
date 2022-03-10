'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.
'''
class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(m) where m is len(word).
    # Space: O(m) because we might need to insert new nodes for the whole word.
    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            nextNode = node.children.get(i, None)
            if nextNode != None:
                node = nextNode
            else:
                newNode = TrieNode()
                node.children[i] = newNode
                node = newNode
        node.wordEnd = True

    # Time: O(m) where m = len(word).
    # Space: O(1).
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            node = node.children.get(i, None)
            if node is None:
                return False
        return node.wordEnd

    # Time: O(m) where m = len(prefix).
    # Space: O(1).
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            node = node.children.get(i, None)
            if node is None:
                return False
        return True

trie = Trie()
trie.insert("apple")
# Expected: True
trie.search("apple")
# Expected: False
trie.search("app")
# Expected: True
trie.startsWith("app")
trie.insert("app")
# Expected: True
trie.search("app")
