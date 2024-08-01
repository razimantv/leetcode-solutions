# Kth smallest amount with single denomination combination

[Problem link](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        val, sign = [1], [-1]
        for x in coins:
            newval, newsign = [], []
            for y, s in zip(val, sign):
                newval.append(math.lcm(x, y))
                newsign.append(-s)
            val += newval
            sign += newsign
        val, sign = val[1:], sign[1:]

        def cnt(n):
            return sum(n // x * s for x, s in zip(val, sign))

        start, end = 0, k * min(coins)
        while end - start > 1:
            mid = (start + end) // 2
            if cnt(mid) < k:
                start = mid
            else:
                end = mid

        return end
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
* [Binary search](/Collections/binary-search.md#binary-search)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
