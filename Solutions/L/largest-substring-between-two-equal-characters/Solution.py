# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ret, seen = -1, {}
        for i, c in enumerate(s):
            if c in seen:
                ret = max(ret, i - seen[c] - 1)
            else:
                seen[c] = i
        return ret
