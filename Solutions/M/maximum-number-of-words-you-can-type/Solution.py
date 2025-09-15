# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        broken = set(broken)
        return sum(
            1 for word in text.split(' ') if all(c not in broken for c in word)
        )
