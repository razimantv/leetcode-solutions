# Special binary string

[Problem link](https://leetcode.com/problems/special-binary-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/special-binary-string/

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        pieces, l, cnt = [], 0, 0
        for r, c in enumerate(s):
            cnt += 1 if c == '1' else -1
            if not cnt:
                pieces.append('1' + self.makeLargestSpecial(s[l + 1:r]) + '0')
                l = r + 1
        return ''. join(sorted(pieces)[::-1])
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Greedy](/Collections/greedy.md#greedy)
