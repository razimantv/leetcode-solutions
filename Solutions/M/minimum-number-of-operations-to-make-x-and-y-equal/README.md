# Minimum number of operations to make x and y equal

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def work(n):
            if n <= y:
                return y - n
            ret = n - y
            for q in [5, 11]:
                if (r := n % q) == 0:
                    ret = min(ret, 1 + work(n // q))
                else:
                    ret = min(ret, r + 1 + work(n // q),
                              q - r + 1 + work(n // q + 1))
            return ret

        return work(x)
```
## Tags

* [Number transformations based on mathematical rules](/Collections/number-transformations-based-on-mathematical-rules.md#number-transformations-based-on-mathematical-rules)
