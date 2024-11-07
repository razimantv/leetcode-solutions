# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(Counter(
            i for x in candidates for i in range(24) if (1 << i) & x
        ). values())
