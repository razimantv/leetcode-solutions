# Kth distinct string in an array

[Problem link](https://leetcode.com/problems/kth-distinct-string-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        good = 0
        for s in arr:
            if cnt[s] == 1:
                good += 1
                if good == k:
                    return s
        return ''
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
