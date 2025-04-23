# Count largest group

[Problem link](https://leetcode.com/problems/count-largest-group/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        ctr = Counter(Counter(
            sum(int(d) for d in str(x)) for x in range(1, n + 1)
        ).values())
        return ctr[max(ctr)]
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
