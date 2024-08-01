# Count tested devices after test operations

[Problem link](https://leetcode.com/problems/count-tested-devices-after-test-operations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution:
    def countTestedDevices(self, battery: List[int]) -> int:
        ret = 0
        for x in battery:
            if x > ret:
                ret += 1
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
