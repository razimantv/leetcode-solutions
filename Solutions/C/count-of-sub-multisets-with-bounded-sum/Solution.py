# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1

        dp = [0] * (r+1)
        dp[0] = 1

        MOD = 10**9+7
        for k, v in cnt.items():
            if not k:
                continue
            dpc = dp. copy()
            for i in range(k, r+1):
                dpc[i] = (dp[i] + dpc[i-k]) % MOD
                dp[i] = (dpc[i] + MOD -
                         (dpc[i-(v+1)*k] if i >= (v+1)*k else 0)
                         ) % MOD

        return (sum(dp[l:]) * (cnt[0]+1)) % MOD
