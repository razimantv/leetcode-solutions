# https://leetcode.com/problems/check-balanced-string/

class Solution:
    def isBalanced(self, num: str) -> bool:
        return int(num) % 11 == 0
