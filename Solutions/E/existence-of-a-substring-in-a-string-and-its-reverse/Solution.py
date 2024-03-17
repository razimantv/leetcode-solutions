# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rs = s[::-1]
        for i in range(len(s) - 1):
            if s[i:i+2] in rs:
                return True
        return False
