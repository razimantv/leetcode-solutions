# https://leetcode.com/problems/count-special-subsequences

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        def frac(x, y):
            g = gcd(x, y)
            return (x // g, y // g)

        n, cnt, ret = len(nums), defaultdict(int), 0
        for r in range(4, n - 2):
            for p in range(r - 3):
                cnt[frac(nums[p], nums[r - 2])] += 1
            for s in range(r + 2, n):
                ret += cnt[frac(nums[s], nums[r])]
        return ret
