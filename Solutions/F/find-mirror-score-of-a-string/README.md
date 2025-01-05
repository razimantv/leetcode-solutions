# Find mirror score of a string

[Problem link](https://leetcode.com/problems/find-mirror-score-of-a-string)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-mirror-score-of-a-string

class Solution:
    def calculateScore(self, s: str) -> int:
        pos = defaultdict(list)
        rev = {
            c: d for c, d in zip(
                string.ascii_lowercase, string.ascii_lowercase[::-1]
            )
        }
        
        ret = 0
        for i, c in enumerate(s):
            if not pos[rev[c]]:
                pos[c].append(i)
            else:
                ret += i - pos[rev[c]].pop()
        return ret
```
## Tags

* [Stack](/Collections/stack.md#stack)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
