# Count submatrices with all ones

[Problem link](https://leetcode.com/problems/count-submatrices-with-all-ones/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        n, ret = len(mat[0]), 0
        cur = [0] * n
        for row in mat:
            stack = [(0, -1, 0)]
            for i, x in enumerate(row):
                cur[i] = (cur[i] + 1) if x else 0
                while stack[-1][0] > cur[i]:
                    stack.pop()
                stack.append(
                    (cur[i], i, stack[-1][2] + cur[i] * (i - stack[-1][1]))
                )
                ret += stack[-1][2]
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
