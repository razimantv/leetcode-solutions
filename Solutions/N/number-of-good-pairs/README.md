# Number of good pairs

[Problem link](https://leetcode.com/problems/number-of-good-pairs/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ret = 0
        for x in nums:
            ret += cnt[x]
            cnt[x] += 1
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
