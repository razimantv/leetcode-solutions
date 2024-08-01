# Last visited integers

[Problem link](https://leetcode.com/problems/last-visited-integers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        seen, ret, n = [], [], 0
        for s in words:
            if s == 'prev':
                ret.append(seen[-1-n] if n < len(seen) else -1)
                n += 1
            else:
                n = 0
                seen. append(int(s))
        return ret
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
