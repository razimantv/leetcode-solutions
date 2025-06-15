# Max difference you can get from changing an integer

[Problem link](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        for i, c in enumerate(s):
            if i == 0 and c != '1':
                n1 = int(''. join((d if d != c else '1') for d in s))
                break
            elif i != 0 and c not in ('0', s[0]):
                n1 = int(''. join((d if d != c else '0') for d in s))
                break
        else:
            n1 = num
        for c in s:
            if c != '9':
                n2 = int(''. join((d if d != c else '9') for d in s))
                break
        else:
            n2 = num
        return n2 - n1
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
