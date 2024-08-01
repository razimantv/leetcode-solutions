# Minimum number of steps to make two strings anagram

[Problem link](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        return sum(max(cs[x] - ct.get(x, 0), 0) for x in cs)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
