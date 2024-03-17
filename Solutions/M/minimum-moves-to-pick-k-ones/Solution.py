# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n, pos = len(nums), [i for i, x in enumerate(nums) if x]
        psum, m = [0] + list(accumulate(pos)), len(pos)
        min2 = max(0, k - maxChanges)
        max2 = min(min2 + 3, m, k)
        ret = 10 ** 10
        for m2 in range(min2, max2 + 1):
            l, r = m2 // 2, (m2 + 1) // 2
            for i in range(l, m - r + 1):
                ret = min(
                    ret,
                    psum[i + r] - psum[i + r - l] -
                    psum[i] + psum[i - l] + (k - m2) * 2
                )
        return ret
