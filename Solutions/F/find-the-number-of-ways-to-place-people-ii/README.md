# Find the number of ways to place people ii

[Problem link](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n, points = len(points), sorted(points, key=lambda x: [x[0], -x[1]])
        ret = 0
        for i in range(n):
            y, worst = points[i][1], 10 ** 10
            for j in range(i - 1, -1, -1):
                yp = points[j][1]
                if y <= yp < worst:
                    ret += 1
                    worst = yp
        return ret
```
## Tags

* [Sorting](/README.md#Sorting) > [Custom](/README.md#Sorting-Custom)
* [Points in 2D plane](/README.md#Points_in_2D_plane)
