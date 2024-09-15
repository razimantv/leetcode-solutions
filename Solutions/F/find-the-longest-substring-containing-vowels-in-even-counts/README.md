# Find the longest substring containing vowels in even counts

[Problem link](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {c: 1 << i for i, c in enumerate('aeiou')}
        first, cur, ret = {0: -1}, 0, 0
        for i, c in enumerate(s):
            cur ^= vowels.get(c, 0)
            ret = max(ret, i - first.setdefault(cur, i))
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Prefix](/Collections/prefix.md#prefix) > [Bitwise operation](/Collections/prefix.md#bitwise-operation)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of first element with same value](/Collections/array-scanning.md#location-of-first-element-with-same-value)
