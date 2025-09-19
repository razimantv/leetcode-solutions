# Design spreadsheet

[Problem link](https://leetcode.com/problems/design-spreadsheet/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet:

    def __init__(self, rows: int):
        self.data = [[0] * rows for _ in range(26)]

    def idx(self, s):
        return ord(s[0]) - ord('A'), int(s[1:]) - 1

    def setCell(self, cell: str, value: int) -> None:
        c, r = self.idx(cell)
        self. data[c][r] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        ret = 0
        for s in formula[1:].split('+'):
            if s[0] < 'A':
                ret += int(s)
            else:
                r, c = self.idx(s)
                ret += self.data[r][c]

        return ret
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
