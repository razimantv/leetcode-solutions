# Number of ways to divide a long corridor

[Problem link](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt, ret = 0, 1
        for i, c in enumerate(corridor):
            if c == 'S':
                cnt += 1
                if cnt == 2:
                    last = i
                elif cnt == 3:
                    ret = (ret * (i - last)) % (10 ** 9 + 7)
                    cnt = 1
        return ret if cnt == 2 else 0
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Location of previous element with same value](/README.md#Array_scanning-Location_of_previous_element_with_same_value)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
