# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last, ret = {c: -1 for c in 'abc'}, 0
        for i, c in enumerate(s):
            last[c] = i
            ret += min(last. values()) + 1
        return ret
