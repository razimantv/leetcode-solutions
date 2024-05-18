# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [math.inf] * n + [0]
        for l in range(n-1, -1, -1):
            cnt = defaultdict(int)
            for r in range(l, n):
                cnt[s[r]] += 1
                if min(cnt.values()) == max(cnt.values()):
                    dp[l] = min(dp[l], dp[r+1] + 1)
        return dp[0]
