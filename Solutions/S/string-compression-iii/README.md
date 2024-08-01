# String compression iii

[Problem link](https://leetcode.com/problems/string-compression-iii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        c, cnt, ret = word[0], 1, ''
        for d in word[1:]:
            if d != c or cnt == 9:
                ret += str(cnt) + c
                c, cnt = d, 1
            else:
                cnt += 1
        return ret + str(cnt) + c
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
