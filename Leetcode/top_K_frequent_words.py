from leetcode import *

class Solution:
    # Quickselect. Other solutions may use a heap or bucket sort.
    # Time: O(n + k*log(k))
    # Space: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Get the frequencies.
        self.freqs = {}
        for i in words:
            self.freqs[i] = self.freqs.setdefault(i, 0) + 1

        # Quickselect algorithm with average case O(n) and worst case O(n^2).
        def select(words: List[str], left: int, right: int, k: int) -> None:
            # If list has only 1 element, then return.
            if left >= right:
                return

            # Select pivot
            pivot = random.randint(left, right)
            pivot = partition(words, left, right, pivot)

            if pivot == k:
                return
            elif pivot < k:
                select(words, pivot + 1, right, k)
            else:
                select(words, left, pivot - 1, k)

        def partition(words: List[str], left: int, right: int, pivot: int) -> int:
            pivotFreq = self.freqs[words[pivot]]
            pivotVal = words[pivot]

            # Swap pivot with the end
            words[pivot], words[right] = words[right], words[pivot]

            j = left
            for i in range(left, right):
                freq = self.freqs[words[i]]
                if freq > pivotFreq:
                    words[i], words[j] = words[j], words[i]
                    j += 1
                elif freq == pivotFreq and words[i] < pivotVal:
                    words[i], words[j] = words[j], words[i]
                    j += 1

            words[right], words[j] = words[j], words[right]
            return j
        
        # Get the kth most frequent from the list of unique words.
        uniqueWords = list(self.freqs.keys())
        select(uniqueWords, 0, len(uniqueWords) - 1, k)
        answer = uniqueWords[:k]

        # Sort kth most frequent words so O(k*log(k)) by highest to lowest frequency and in lexicographical order.
        answer.sort(key=lambda x:(-self.freqs[x], x))
        return answer

solution = Solution()

# Expected: ["i","love"]
print(solution.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))

# Expected: ["the","is","sunny","day"]
print(solution.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
