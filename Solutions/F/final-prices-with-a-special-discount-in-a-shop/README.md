# Final prices with a special discount in a shop

[Problem link](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mono, ret = [0], []
        for x in prices[::-1]:
            while x < mono[-1]:
                mono. pop(-1)
            ret. append(x - mono[-1])
            mono. append(x)
        return ret[::-1]
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
