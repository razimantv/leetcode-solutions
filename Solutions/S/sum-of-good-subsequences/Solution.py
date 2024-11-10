# https://leetcode.com/problems/sum-of-good-subsequences/

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        cnt, tot = defaultdict(int), defaultdict(int)
        ret, mod = 0, 10 ** 9 + 7

        for x in nums:
            newcnt = (1 + cnt[x - 1] + cnt[x + 1]) % mod
            newtot = (tot[x - 1] + tot[x + 1] + x * newcnt) % mod
            ret = (ret + newtot) % mod
            cnt[x] = (cnt[x] + newcnt) % mod
            tot[x] = (tot[x] + newtot) % mod
        return ret
