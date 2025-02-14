# Product of the last k numbers

[Problem link](https://leetcode.com/problems/product-of-the-last-k-numbers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.zeros, self.product = [0], [1]

    def add(self, num: int) -> None:
        z, p = self. zeros, self. product
        if num:
            z.append(z[-1])
            p.append(p[-1] * num)
        else:
            z.append(z[-1] + 1)
            p.append(p[-1])

    def getProduct(self, k: int) -> int:
        z, p = self. zeros, self. product
        return p[-1] // p[-1 - k] if z[-1] == z[-1 - k] else 0
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
