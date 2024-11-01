# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        return ''.join(c for i, c in enumerate(s) if s[i:i+3] != c * 3)
