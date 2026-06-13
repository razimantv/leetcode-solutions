# https://leetcode.com/problems/weighted-word-mapping/

class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        return ''. join(
            chr(ord('z') - sum(weights [ord(c) - ord('a')] for c in word) % 26)
            for word in words
        )
