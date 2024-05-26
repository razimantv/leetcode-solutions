# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

class Solution:
    def waysToReachStair(self, k: int) -> int:
        def choose(n, r):
            r, ret = min(r, n - r), 1
            for i in range(r):
                ret = ret * (n - i) // (i + 1)
            return ret

        pos, i, ret = 1, 0, 1 if k <= 1 else 0
        while True:
            pos += 1 << i
            i += 1
            if pos - (i + 1) > k:
                break
            sub = pos - k
            if sub >= 0:
                ret += choose(i + 1, sub)
        return ret
