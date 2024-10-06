# Sorted gcd pair queries

[Problem link](https://leetcode.com/problems/sorted-gcd-pair-queries/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sorted-gcd-pair-queries/

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        nmax = max(nums)
        gcnt, ctr = [0] * (nmax + 1), [0] * (nmax + 1)
        for x in nums:
            ctr[x] += 1

        for i in range(nmax, 0, -1):
            j, cur = i, 0
            for j in range(i, nmax + 1, i):
                gcnt[i] -= gcnt[j]
                cur += ctr[j]
            gcnt[i] += cur * (cur - 1) // 2

        psum = list(accumulate(gcnt))
        return [bisect_right(psum, q) for q in queries]
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Dynamic programming](/Collections/mathematics.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Prime sieving](/Collections/mathematics.md#prime-sieving)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
