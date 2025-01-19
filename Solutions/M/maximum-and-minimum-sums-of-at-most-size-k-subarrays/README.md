# Maximum and minimum sums of at most size k subarrays

[Problem link](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

class Solution:
    def minMaxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def cnt(l, m, r):
            l, r = max(l, m - k + 1), min(r, m + k - 1)
            if l + k - 1 >= r:
                return (m - l + 1) * (r - m + 1)
            l1, nmin = r - k + 1, l + k - m
            return (r - m + nmin) * (l1 - l) // 2 + (m - l1 + 1) * (r - m + 1)

        def mintot(ar):
            mono, start, end = [], [0] * n, [n - 1] * n
            for i, x in enumerate(ar):
                while mono and ar[mono[-1]] > x:
                    end[mono.pop()] = i - 1
                start[i] = (mono[-1] + 1) if mono else 0
                mono.append(i)
            return sum(x * cnt(start[i], i, end[i]) for i, x in enumerate(ar))

        return mintot(nums) - mintot([-x for x in nums])
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
