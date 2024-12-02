# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, search: str) -> int:
        n = len(search)
        for i, word in enumerate(sentence.split()):
            if word[:n] == search:
                return i + 1
        return -1
