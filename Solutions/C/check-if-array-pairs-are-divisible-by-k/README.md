# Check if array pairs are divisible by k

[Problem link](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter()
        for x in arr:
            x %= k
            if cnt[(k - x) % k]:
                cnt[(k - x) % k] -= 1
            else:
                cnt[x] += 1
        return not any(cnt.values())
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
