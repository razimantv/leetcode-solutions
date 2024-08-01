# Maximum square area by removing fences from a field

[Problem link](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        def diffs(ar):
            return set([
                abs(ar[i] - ar[j])
                for i in range(len(ar)) for j in range(i)
            ])

        diffh = diffs([1] + hFences + [m])
        diffv = diffs([1] + vFences + [n])
        hmax = max(diffv.intersection(diffh), default=-1)
        return -1 if hmax == -1 else ((hmax ** 2) % (10 ** 9 + 7))
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
