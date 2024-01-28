# https://leetcode.com/problems/number-of-changing-keys/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(1 for c1, c2 in pairwise(s) if c1.lower() != c2.lower())
