# https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((ord('z') + 1 - ord(c)) * (i + 1) for i, c in enumerate(s))
