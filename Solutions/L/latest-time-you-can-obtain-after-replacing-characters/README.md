# Latest time you can obtain after replacing characters

[Problem link](https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution:
    def findLatestTime(self, s: str) -> str:
        h, m = s. split(':')

        def work(ss, lim):
            for x in range(lim):
                xs = f'{x:02}'
                if all(c == d or c == '?' for c, d in zip(ss, xs)):
                    ret = xs
            return ret

        return work(h, 12) + ':' + work(m, 60)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
