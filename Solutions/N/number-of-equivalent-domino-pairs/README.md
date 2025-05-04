# Number of equivalent domino pairs

[Problem link](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        return sum(
            x * (x - 1) // 2
            for x in Counter(tuple(sorted(d)) for d in dominoes).values()
        )
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
