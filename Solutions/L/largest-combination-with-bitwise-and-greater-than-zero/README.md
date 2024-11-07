# Largest combination with bitwise and greater than zero

[Problem link](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(Counter(
            i for x in candidates for i in range(24) if (1 << i) & x
        ). values())
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
