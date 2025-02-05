# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        bad = [i for i, (c, d) in enumerate(zip(s1, s2)) if c != d]
        return not bad or (
            len(bad) == 2 and
            (s1[bad[0]], s1[bad[1]]) == (s2[bad[1]], s2[bad[0]])
        )
