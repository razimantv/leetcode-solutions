# Sort the jumbled numbers

[Problem link](https://leetcode.com/problems/sort-the-jumbled-numbers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(n):
            return int(''.join(map(lambda x: str(mapping[int(x)]), str(n))))
        return sorted(nums, key=convert)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
