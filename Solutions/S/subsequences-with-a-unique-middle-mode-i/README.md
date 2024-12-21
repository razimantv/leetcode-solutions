# Subsequences with a unique middle mode i

[Problem link](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i

class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        n, ctr, left, ret = len(nums), Counter(nums), Counter(), 0
        for i, x in enumerate(nums):
            if ctr[x] == 1:
                left[x] += 1
                continue
            ret += (
                (lx := left[x]) * (lx - 1) *
                (rx := (ctr[x] - lx - 1)) * (rx - 1) // 4
            )
            ret += (
                lx * (i - lx) * rx * (rx - 1) // 2 +
                rx * (n - i - 1 - rx) * lx * (lx - 1) // 2
            )
            ret += (
                lx * (lx - 1) * (n - i - 1 - rx) * (n - i - 2 - rx) // 4 +
                (i - lx) * (i - lx - 1) * rx * (rx - 1) // 4 +
                lx * (i - lx) * rx * (n - i - 1 - rx)
            )
            l2, r2, lnotx, rnotx = 0, 0, 0, 0
            for k, v in ctr. items():
                if k == x:
                    continue
                vl = left[k]
                vr = v - vl
                l2 += vl * lnotx
                r2 += vr * rnotx
                lnotx += vl
                rnotx += vr
            for k, v in ctr.items():
                if k == x:
                    continue
                vl = left[k]
                vr = v - vl
                ret += (
                    lx * vl * (r2 - vr * (rnotx - vr)) +
                    rx * vr * (l2 - vl * (lnotx - vl))
                )
            left[x] += 1
        return ret % (10 ** 9 + 7)
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
* [Case-by-case analysis](/Collections/case-by-case-analysis.md#case-by-case-analysis)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Middle element of triplet](/Collections/array-scanning.md#middle-element-of-triplet)
