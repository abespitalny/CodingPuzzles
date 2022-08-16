'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''
from leetcode import *

class Solution:
    # Time: O(m + n) where m are the number of characters in paragraph and n is the number of characters in banned.
    # Space: O(m + n)
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedSet = set(banned)
        punctuation = {" ", "!", "?", "'", ",", ";", "."}

        wordCount = {}
        highestCount = 0
        highestCountWord = ""

        wordBuilder = []
        paragraph += "."
        for i, char in enumerate(paragraph):
            if char not in punctuation:
                wordBuilder.append(char.lower())
            elif len(wordBuilder) != 0:
                word = ''.join(wordBuilder)
                if word not in bannedSet:
                    count = wordCount.get(word, 0) + 1
                    wordCount[word] = count
                    
                    if count > highestCount:
                        highestCount = count
                        highestCountWord = word

                wordBuilder = []

        return highestCountWord

solution = Solution()

assert solution.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]) == "ball"
assert solution.mostCommonWord(paragraph = "a.", banned = []) == "a"
