# Letter tile possibilities

[Problem link](https://leetcode.com/problems/letter-tile-possibilities)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/letter-tile-possibilities

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        @cache
        def work(mask):
            if not mask:
                return set([''])
            ret = set()
            for i in range(len(tiles)):
                if not (mask & (1 << i)):
                    continue
                cur = work(mask ^ (1 << i))
                for s in cur:
                    ret.add(s)
                    ret.add(s + tiles[i])

            return ret

        return len(work((1 << len(tiles)) - 1)) - 1
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Backtracking](/Collections/backtracking.md#backtracking)
