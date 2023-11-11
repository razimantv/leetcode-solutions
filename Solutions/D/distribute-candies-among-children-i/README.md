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

* [Mathematics](/README.md#Mathematics) > [Closed form expressions](/README.md#Mathematics-Closed_form_expressions)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics) > [Inclusion-exclusion](/README.md#Mathematics-Combinatorics-Inclusion_exclusion)
