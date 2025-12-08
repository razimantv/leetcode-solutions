# Count square sum triples

[Problem link](https://leetcode.com/problems/count-square-sum-triples/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        squares, ret = set((i * i for i in range(1, n + 1))), 0
        for i in range(4, n):
            for j in range(3, i):
                if (cur := i ** 2 + j ** 2) > n ** 2:
                    break
                elif cur in squares:
                    ret += 2
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
