# https://leetcode.com/problems/count-commas-in-range/

class Solution:
    def countCommas(self, n: int) -> int:
        return sum((len(str(x)) - 1) // 3 for x in range(n + 1))
