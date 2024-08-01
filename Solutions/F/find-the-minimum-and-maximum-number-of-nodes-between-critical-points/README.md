# Find the minimum and maximum number of nodes between critical points

[Problem link](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class Solution:
    def nodesBetweenCriticalPoints(
        self, head: Optional[ListNode]
    ) -> List[int]:
        first, last, pos, m = 0, 0, 0, math.inf
        next, after = head.next, head.next.next
        while after:
            pos += 1
            if (next.val - head.val) * (next.val - after.val) > 0:
                if not first:
                    first, last = pos, pos
                else:
                    diff = pos - last
                    last = pos
                    m = min(m, diff)
            head, next, after = next, after, after.next
        return [-1, -1] if m > pos else [m, last - first]
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
