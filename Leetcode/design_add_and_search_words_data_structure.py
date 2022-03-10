from implement_trie import TrieNode, Trie

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    # Time: O(26^m) where m = len(word) because there can be at most 26 (the alphabet) children for a node.
    # Space: O(26^m).
    def search(self, word: str) -> bool:
        def searchDFS(root: TrieNode, wordPos: int) -> bool:
            while wordPos < len(word):
                if word[wordPos] == '.':
                    for i in root.children:
                        if searchDFS(root.children[i], wordPos + 1):
                            return True
                    return False
                else:
                    root = root.children.get(word[wordPos], None)
                    if root is None:
                        return False
                    wordPos += 1
            return root.wordEnd

        return searchDFS(self.trie.root, 0)

    # Stole this from leetcode. Uses BFS instead of DFS.
    def searchV2(self, word: str) -> bool:
        nodes = [self.trie.root]
        for i in word:
            nextNodes = []
            for node in nodes:
                if i == '.':
                    nextNodes.extend([node.children[j] for j in node.children])
                else:
                    nextNode = node.children.get(i, None)
                    if nextNode != None:
                        nextNodes.append(nextNode)
            
            nodes = nextNodes

        for node in nodes:
            if node.wordEnd:
                return True
        return False     

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
# Expected: False
print(wordDictionary.search("pad"))
# Expected: True
print(wordDictionary.search("bad"))
# Expected: True
print(wordDictionary.search(".ad"))
# Expected: True
print(wordDictionary.search("b.."))
