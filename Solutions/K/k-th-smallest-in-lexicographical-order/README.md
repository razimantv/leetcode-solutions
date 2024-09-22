# K th smallest in lexicographical order

[Problem link](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(x):
            ret, p10 = 0, 1
            while x <= n:
                ret += min(p10, n - x + 1)
                x, p10 = x * 10, p10 * 10
            return ret

        x = 0
        while x * 10 <= n:
            for d in range(x == 0, 10):
                y = x * 10 + d
                if k == 1:
                    return y

                cur = count(y)
                if cur >= k:
                    x, k = y, k - 1
                    break
                else:
                    k -= cur
        return x
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
