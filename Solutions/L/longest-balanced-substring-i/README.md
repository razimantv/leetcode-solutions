# Longest balanced substring i

[Problem link](https://leetcode.com/problems/longest-balanced-substring-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-balanced-substring-i/

class Solution:
    def longestBalanced(self, s: str) -> int:
        n, ret = len(s), 0
        for i in range(n):
            ctr = defaultdict(int)
            for j in range(i, n):
                ctr[s[j]] += 1
                if len(set(ctr. values())) == 1:
                    ret = max(ret, j - i + 1)
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
