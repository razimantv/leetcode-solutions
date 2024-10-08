# Minimum number of swaps to make the string balanced

[Problem link](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        cur, ret = 0, 0
        for c in s:
            cur += 1 if c == '[' else -1
            if cur < 0:
                ret += 1
                cur = 1
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [Valid brackets](/Collections/prefix.md#valid-brackets)
* [Greedy](/Collections/greedy.md#greedy)
