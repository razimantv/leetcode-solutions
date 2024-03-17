# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        x = Counter(s)[c]
        return x * (x + 1) // 2
