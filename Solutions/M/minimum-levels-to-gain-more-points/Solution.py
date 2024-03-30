# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        ctr = Counter(possible)
        tot, cur = ctr[1] - ctr[0], 0
        for i, x in enumerate(possible[:-1]):
            cur += 1 if x else -1
            if cur * 2 > tot:
                return i + 1
        return -1
