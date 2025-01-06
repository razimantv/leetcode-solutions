# Minimum number of operations to move all balls to each box

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ret = [0] * n

        cnt, tot = 0, 0
        for i in range(n):
            tot += cnt
            ret[i] += tot
            cnt += boxes[i] == '1'

        cnt, tot = 0, 0
        for i in range(n - 1, -1, -1):
            tot += cnt
            ret[i] += tot
            cnt += boxes[i] == '1'

        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
