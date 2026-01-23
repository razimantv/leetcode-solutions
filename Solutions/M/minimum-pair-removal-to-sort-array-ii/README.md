# Minimum pair removal to sort array ii

[Problem link](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii

from sortedcontainers import SortedList


class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n, ret = len(nums), 0
        adjsums, badpairs = SortedList(), set()
        left, right = list(range(-1, n - 1)), list(range(1, n + 1))
        for i, (x, y) in enumerate(pairwise(nums)):
            adjsums.add((x + y, i, i + 1))
            if x > y:
                badpairs.add((i, i + 1))

        while badpairs:
            ret += 1
            tot, l, r = adjsums.pop(0)
            if (l, r) in badpairs:
                badpairs.remove((l, r))
            if left[l] != -1:
                adjsums.remove((nums[l] + nums[left[l]], left[l], l))
                if (left[l], l) in badpairs:
                    badpairs.remove((left[l], l))
                adjsums.add((tot + nums[left[l]], left[l], l))
                if nums[left[l]] > tot:
                    badpairs.add((left[l], l))
                right[l] = right[r]
            if right[r] != n:
                adjsums.remove((nums[r] + nums[right[r]], r, right[r]))
                if (r, right[r]) in badpairs:
                    badpairs.remove((r, right[r]))
                adjsums.add((tot + nums[right[r]], l, right[r]))
                if tot > nums[right[r]]:
                    badpairs.add((l, right[r]))
                left[right[r]] = l
            nums[l] = tot

        return ret
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)
* [Linked list](/Collections/linked-list.md#linked-list) > [Knuths Algorithm X](/Collections/linked-list.md#knuths-algorithm-x)
* [Hashmap](/Collections/hashmap.md#hashmap)
