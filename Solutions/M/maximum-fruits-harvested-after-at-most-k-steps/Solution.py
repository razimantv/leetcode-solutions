# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution:
    def maxTotalFruits(
        self, fruits: list[list[int]], start: int, k: int
    ) -> int:
        pos, cnt = (list(x) for x in zip(*fruits))

        def work(pos, cnt, start):
            psum = [0] + list(accumulate(cnt))
            bad, ret = bisect_right(pos, start), 0
            for i, x in enumerate(pos):
                if x > start:
                    break
                elif start - x > k:
                    continue
                cur = psum[bad] - psum[i]
                if (delta := k - 2 * (start - x)) > 0:
                    end = bisect_right(pos, start + delta)
                    cur += psum[end] - psum[bad]
                ret = max(ret, cur)
            return ret

        return max(
            work(pos, cnt, start),
            work([-x for x in pos[::-1]], cnt[::-1], -start)
        )
