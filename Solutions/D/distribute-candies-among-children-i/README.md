# Distribute candies among children i

[Problem link](https://leetcode.com/problems/distribute-candies-among-children-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/distribute-candies-among-children-i/

class Solution:
    def starsbars(self, n):
        if n < 0:
            return 0
        return (n+2) * (n+1) // 2

    def distributeCandies(self, n: int, limit: int) -> int:
        limit += 1
        return (
            self.starsbars(n) -
            3 * self.starsbars(n-limit) +
            3 * self.starsbars(n-2*limit) -
            self.starsbars(n-3*limit)
        )
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
