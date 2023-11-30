# Minimum one bit operations to make integers zero

[Problem link](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def dp0(n):
            if n < 2:
                return n

            k = 0
            while 1 << (k+1) <= n:
                k += 1

            return dp1(n ^ (1 << k), k-1) + (1 << k)

        def dp1(n, k):
            if k == 0:
                return 1 - n
            elif n & (1 << k):
                return dp0(n ^ (1 << k))
            else:
                return dp1(n, k-1) + (1 << k)

        return dp0(n)
```
## Tags

* [Bitwise operation](/README.md#Bitwise_operation)
* [Dynamic programming](/README.md#Dynamic_programming) > [Auxiliary array](/README.md#Dynamic_programming-Auxiliary_array)
