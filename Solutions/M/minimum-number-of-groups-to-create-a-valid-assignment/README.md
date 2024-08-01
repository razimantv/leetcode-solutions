# Minimum number of groups to create a valid assignment

[Problem link](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for x in nums:
            d[x] += 1

        vals = sorted([v for k, v in d.items()])
        if len(vals) == 1:
            return 1

        for x in range(vals[0], 0, -1):
            good = True
            cur = 0
            for v in vals:
                if v % (x+1) == 0:
                    b = v // (x+1)
                    cur += b
                    continue
                a = v // x
                b = v % x
                if b > a:
                    good = False
                    break
                a -= b
                b += (a // (x+1)) * x
                a %= (x+1)
                cur += a + b
            if good:
                best = cur
                break
        return best
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
