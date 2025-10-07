# Avoid flood in the city

[Problem link](https://leetcode.com/problems/avoid-flood-in-the-city/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        last, zeros = {}, SortedList()
        for i, x in enumerate(rains):
            if x == 0:
                zeros.add(i)
            elif x in last:
                idx = zeros. bisect_right(last[x])
                if idx == len(zeros):
                    return []
                rains[zeros[idx]] = -x
                zeros.pop(idx)
                last[x] = i
            else:
                last[x] = i
        return [(-1 if x > 0 else 1 if x == 0 else -x) for x in rains]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Binary search](/Collections/binary-search.md#binary-search) > [Python SortedList](/Collections/binary-search.md#python-sortedlist)
* [Greedy](/Collections/greedy.md#greedy)
