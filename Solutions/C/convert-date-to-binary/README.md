# Convert date to binary

[Problem link](https://leetcode.com/problems/convert-date-to-binary/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/convert-date-to-binary/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(f'{int(x):b}' for x in date.split('-'))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
