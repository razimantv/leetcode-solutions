# Longest balanced substring ii

[Problem link](https://leetcode.com/problems/longest-balanced-substring-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-balanced-substring-ii/

class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt, first, ret = [0] * 3, [{(0, 0): -1} for _ in range(7)], 0
        for i, x in enumerate(s):
            cnt[ord(x) - ord('a')] += 1
            a, b, c = cnt
            tuples = [
                (a, b), (a, c), (b, c),
                (a - b, c), (a - c, b), (b - c, a),
                (a - b, b - c)
            ]
            for j, t in enumerate(tuples):
                if t not in first[j]:
                    first[j][t] = i
                ret = max(ret, i - first[j][t])
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Hashmap](/Collections/hashmap.md#hashmap)
