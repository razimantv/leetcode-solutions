# High access employees

[Problem link](https://leetcode.com/problems/high-access-employees/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/high-access-employees/

class Solution:
    def findHighAccessEmployees(self, access: List[List[str]]) -> List[str]:
        access = sorted(access)
        ret = {}
        for i in range(2, len(access)):
            if access[i-2][0] == access[i][0] and (
                int(access[i][1]) - int(access[i-2][1])
            ) < 100:
                ret[access[i][0]] = 1
        return [k for k in ret]
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
