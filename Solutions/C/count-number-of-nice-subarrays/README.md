# Count number of nice subarrays

[Problem link](https://leetcode.com/problems/count-number-of-nice-subarrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt, cur, ret = {0: 1}, 0, 0
        for x in nums:
            cur += x & 1
            if cur >= k:
                ret += cnt[cur - k]
            cnt[cur] = 1 if x & 1 else cnt[cur] + 1
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Hashmap](/Collections/hashmap.md#hashmap)
