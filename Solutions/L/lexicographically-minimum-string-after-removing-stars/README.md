# Lexicographically minimum string after removing stars

[Problem link](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution:
    def clearStars(self, s: str) -> str:
        seen = defaultdict(list)
        for i, c in enumerate(s):
            if c == '*':
                d = min(seen)
                seen[d].pop()
                if not seen[d]:
                    seen.pop(d)
            else:
                seen[c].append(i)
        return ''.join(
            c for i, c in sorted([(i, c) for c, v in seen.items() for i in v])
        )
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Greedy](/Collections/greedy.md#greedy)
