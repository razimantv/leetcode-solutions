# Maximum score from grid operations

[Problem link](https://leetcode.com/problems/maximum-score-from-grid-operations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-score-from-grid-operations/

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        dp_inc, dp_exc = [[[0] * (m + 1) for _ in range(m + 1)]
                          for __ in (0, 1)]
        psum = [
            [0] + list(accumulate(column)) for column in zip(*grid)
        ]
        for s1, s2 in pairwise(psum):
            newdp_inc, newdp_exc = [
                [[0] * (m + 1) for _ in range(m + 1)] for __ in (0, 1)]
            for i in range(m + 1):
                for j in range(m + 1):
                    if i <= j:
                        newdp_inc[i][j] = dp_inc[j][0] + s2[j] - s2[i]
                        newdp_exc[i][j] = dp_inc[j][0]
                    else:
                        newdp_inc[i][j] = newdp_exc[i][j] = max(
                            dp_inc[j][i], dp_exc[j][i] + s1[i] - s1[j])
                for j in range(1, m + 1):
                    newdp_exc[i][j] = max(newdp_exc[i][j-1], newdp_exc[i][j])
                    newdp_inc[i][-1-j] = max(newdp_inc[i]
                                             [-1-j], newdp_inc[i][-j])
            dp_inc, dp_exc = newdp_inc, newdp_exc
        return max(dp[0] for dp in dp_inc)
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
