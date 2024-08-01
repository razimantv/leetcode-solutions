# Minimum number of pushes to type word ii

[Problem link](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(
            (i // 8 + 1) * x for i, x in enumerate(
                sorted(Counter(word).values(), reverse=True)
            )
        )
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
