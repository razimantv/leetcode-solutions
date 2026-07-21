# Maximize active section with trade i

[Problem link](https://leetcode.com/problems/maximize-active-section-with-trade-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        prev, cur, ret = 0, 0, 0
        for c in s:
            if c == '0':
                cur += 1
                if prev:
                    ret = max(ret, cur + prev)
            else: 
                if cur:
                    prev, cur = cur, 0
        return ret + Counter(s)['1']
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
