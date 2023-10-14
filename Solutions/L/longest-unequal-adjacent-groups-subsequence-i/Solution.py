# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        s0, s1 = [], []
        for w, g in zip(words, groups):
            if g and len(s0) >= len(s1):
                s1 = s0 + [w]
            elif not g and len(s1) >= len(s0):
                s0 = s1 + [w]
        return s0 if len(s0) > len(s1) else s1
