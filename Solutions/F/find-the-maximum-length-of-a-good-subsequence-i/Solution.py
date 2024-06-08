# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = defaultdict(list)
        best = [0]
        for x in nums:
            l = min(k, len(best))
            cur = dp[x]
            if len(cur) <= l:
                cur += [0] * (l + 1 - len(cur))
            if len(best) <= l:
                best += [0] * (l + 1 - len(best))
            for i in range(l, -1, -1):
                cur[i] = max(cur[i], best[i - 1] if i else 0) + 1
                best[i] = max(best[i], cur[i])
        return max(best)
