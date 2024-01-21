# Minimum number of pushes to type word i

[Problem link](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(
            (i // 8 + 1) * x for i, x in enumerate(
                sorted(Counter(word).values(), reverse=True)
            )
        )
```
## Tags

* [Greedy](/README.md#Greedy)
* [Hashmap](/README.md#Hashmap) > [Counter](/README.md#Hashmap-Counter)
