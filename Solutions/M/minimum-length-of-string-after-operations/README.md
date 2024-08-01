# Minimum length of string after operations

[Problem link](https://leetcode.com/problems/minimum-length-of-string-after-operations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        ret = 0
        for x in Counter(s).values():
            while x >= 3:
                x -= 2
            ret += x
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
