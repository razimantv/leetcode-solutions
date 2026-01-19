# Maximum side length of a square with sum less than or equal to threshold

[Problem link](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        start = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                mat[i][j] += (
                    (mat[i - 1][j] if i else 0) + (mat[i][j - 1] if j else 0) -
                    (mat[i - 1][j - 1] if (i and j) else 0)
                )

                end = min(i, j) + 2
                while end - start > 1:
                    mid = (start + end) // 2
                    cur = (
                        mat[i][j] - (mat[i - mid][j] if i >= mid else 0) -
                        (mat[i][j - mid] if j >= mid else 0) +
                        (mat[i - mid][j - mid] if min(i, j) >= mid else 0)
                    )

                    if cur <= threshold:
                        start = mid
                    else:
                        end = mid

        return start
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [Prefix sum](/Collections/binary-search.md#prefix-sum)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
