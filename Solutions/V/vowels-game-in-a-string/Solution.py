# https://leetcode.com/problems/vowels-game-in-a-string/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return True if any(c for c in 'aeiou' if c in s) else False
