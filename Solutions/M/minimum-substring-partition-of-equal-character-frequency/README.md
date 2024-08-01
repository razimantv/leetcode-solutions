# Minimum substring partition of equal character frequency

[Problem link](https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/)

## Solutions


### Solution.py
```py
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
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
