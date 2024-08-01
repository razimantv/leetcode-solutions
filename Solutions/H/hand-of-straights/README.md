# Hand of straights

[Problem link](https://leetcode.com/problems/hand-of-straights/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/hand-of-straights/

from sortedcontainers import SortedList


class Solution:
    def isNStraightHand(self, hand: List[int], group: int) -> bool:
        sl = SortedList(map(list, Counter(hand).items()))

        while sl:
            x, cnt = sl.pop()
            if not cnt:
                continue
            elif len(sl) < group - 1:
                return False
            for i in range(1, group):
                if sl[-i] < [x - i, cnt]:
                    return False
                sl[-i][1] -= cnt
        return True
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
