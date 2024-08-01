# Find the encrypted string

[Problem link](https://leetcode.com/problems/find-the-encrypted-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-encrypted-string/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        return ''.join([s[(i + k) % n] for i in range(n)])
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
