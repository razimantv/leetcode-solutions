# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution:
    def maxDifference(self, s: str) -> int:
        ctr = Counter(s)
        odd, even = [[x for x in ctr.values() if (x & 1) == p] for p in [1, 0]]
        return max(odd) - min(even)
