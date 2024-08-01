# Grumpy bookstore owner

[Problem link](https://leetcode.com/problems/grumpy-bookstore-owner/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        no, yes, l, cur = 0, 0, 0, 0
        for r, (x, y) in enumerate(zip(customers, grumpy)):
            if y:
                cur += x
            else:
                no += x
            if r - l == minutes:
                if grumpy[l]:
                    cur -= customers[l]
                l += 1
            yes = max(yes, cur)
        return yes + no
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
