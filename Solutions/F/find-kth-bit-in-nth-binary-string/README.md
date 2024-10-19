# Find kth bit in nth binary string

[Problem link](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip, msb = 0, 1 << 20
        while k > 1 and msb:
            if msb & k:
                k = msb - (msb ^ k)
                flip ^= 1
            msb >>= 1
        return str(flip)
```
### Solution2.py
```py
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        a, b = 1, 3
        while k > b:
            a, b = b, 2 * b + 1
        flip = 0
        while True:
            if k == 1:
                break
            elif k == a + 1:
                return str(1 ^ flip)
            if k > a + 1:
                k = b - k + 1
                flip ^= 1
            a, b = a // 2, a
        return str(flip)
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Divide and conquer](/Collections/divide-and-conquer.md#divide-and-conquer)
