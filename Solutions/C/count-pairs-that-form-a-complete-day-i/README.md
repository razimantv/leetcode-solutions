# Count pairs that form a complete day i

[Problem link](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = defaultdict(int)
        ret = 0
        for x in hours:
            ret += cnt[(24 - x % 24) % 24]
            cnt[x % 24] += 1
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
