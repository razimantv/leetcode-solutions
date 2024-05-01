# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return word[i::-1] + word[i + 1:]
        return word
