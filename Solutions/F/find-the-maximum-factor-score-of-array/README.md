# Find the maximum factor score of array

[Problem link](https://leetcode.com/problems/find-the-maximum-factor-score-of-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution:
    def maxScore(self, ar: List[int]) -> int:
        def score(ar):
            if not ar:
                return 0
            l, g = ar[0], ar[0]
            for x in ar[1:]:
                g = gcd(g, x)
                l = l * x // gcd(l, x)
            return l * g

        ret = score(ar)
        for i in range(len(ar)):
            ret = max(ret, score(ar[:i] + ar[i + 1:]))
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
