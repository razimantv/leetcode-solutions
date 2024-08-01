# Maximum xor product

[Problem link](https://leetcode.com/problems/maximum-xor-product/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-xor-product/

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mask = a ^ b
        ret = sorted([x ^ (((1 << n)-1) & x) for x in (a, b)])
        idx = 1 if ret[1] == ret[0] else 0
        print(ret, idx)
        for i in range(n-1, -1, -1):
            cur = 1 << i
            if mask & cur:
                ret[idx] |= cur
                idx = 0
            else:
                ret[0] |= cur
                ret[1] |= cur
        return (ret[0] * ret[1]) % (10**9 + 7)
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Greedy](/Collections/greedy.md#greedy)
