# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string

class Solution:
    def findValidPair(self, s: str) -> str:
        ctr = Counter(s)
        for x, y in pairwise(s):
            if x != y and ctr[x] == int(x) and ctr[y] == int(y):
                return x + y
        return ""
