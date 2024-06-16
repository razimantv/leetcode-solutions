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

* [Hashmap](/README.md#Hashmap) > [Counter](/README.md#Hashmap-Counter)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
