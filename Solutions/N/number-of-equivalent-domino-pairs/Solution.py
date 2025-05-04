# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        return sum(
            x * (x - 1) // 2
            for x in Counter(tuple(sorted(d)) for d in dominoes).values()
        )
