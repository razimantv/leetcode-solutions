# Maximum manhattan distance after k changes

[Problem link](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ctr, ret = Counter(), 0
        for c in s:
            ctr[c] += 1
            good = max(ctr['N'], ctr['S']) + max(ctr['E'], ctr['W'])
            bad = min(ctr['N'], ctr['S']) + min(ctr['E'], ctr['W'])
            ret = max(ret, good - bad + 2 * min(k, bad))
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Greedy](/Collections/greedy.md#greedy)
