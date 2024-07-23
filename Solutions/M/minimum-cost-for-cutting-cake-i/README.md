# Minimum cost for cutting cake i

[Problem link](https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution:
    def minimumCost(
        self, m: int, n: int, horizontal: List[int], vertical: List[int]
    ) -> int:
        horizontal.sort(reverse=True)
        vertical.sort(reverse=True)
        m, n = m - 1, n - 1
        ret = 0
        i, j = 0, 0
        while i < m or j < n:
            if i == m or (j != n and horizontal[i] < vertical[j]):
                ret += (i + 1) * vertical[j]
                j += 1
            else:
                ret += (j + 1) * horizontal[i]
                i += 1
        return ret
```
## Tags

* [Greedy](/README.md#Greedy)