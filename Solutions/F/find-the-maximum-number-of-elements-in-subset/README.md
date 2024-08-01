# Find the maximum number of elements in subset

[Problem link](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        best = max(1, ctr[1] - (0 if ctr[1] % 2 else 1))
        for k, v in ctr.items():
            if k == 1 or v == 1:
                continue
            cur = 1
            while k in ctr and ctr[k] >= 2:
                cur += 2
                k *= k
            if k not in ctr:
                cur -= 2
            best = max(best, cur)
        return best
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
