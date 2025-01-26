# Count mentions per user

[Problem link](https://leetcode.com/problems/count-mentions-per-user)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-mentions-per-user

class Solution:
    def countMentions(self, n: int, events: list[list[str]]) -> list[int]:
        ret, offline = [0] * n, [0] * n
        pq = sorted([
            (int(time), 2 if event == "MESSAGE" else 1, s)
            for event, time, s in events
        ])
        while pq:
            time, event, s = heappop(pq)
            if event == 2:
                if s == "ALL":
                    ids = range(n)
                elif s == "HERE":
                    ids = [i for i, x in enumerate(offline) if not x]
                else:
                    ids = [int(x[2:]) for x in s.split(' ')]
                for id in ids:
                    ret[id] += 1
            else:
                offline[int(s)] = event
                if event:
                    heappush(pq, (time + 60, 0, s))
        return ret
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
