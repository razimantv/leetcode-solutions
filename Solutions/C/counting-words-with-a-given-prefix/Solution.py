# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        L = len(pref)
        return sum(1 for word in words if word[:L] == pref)
