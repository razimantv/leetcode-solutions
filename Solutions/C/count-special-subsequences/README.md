# Count special subsequences

[Problem link](https://leetcode.com/problems/count-special-subsequences)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-special-subsequences

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        def frac(x, y):
            g = gcd(x, y)
            return (x // g, y // g)

        n, cnt, ret = len(nums), defaultdict(int), 0
        for r in range(4, n - 2):
            for p in range(r - 3):
                cnt[frac(nums[p], nums[r - 2])] += 1
            for s in range(r + 2, n):
                ret += cnt[frac(nums[s], nums[r])]
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [GCD/LCM](/Collections/mathematics.md#gcd-lcm)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Expression rearrangement](/Collections/mathematics.md#expression-rearrangement)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Middle element of triplet](/Collections/array-scanning.md#middle-element-of-triplet)
