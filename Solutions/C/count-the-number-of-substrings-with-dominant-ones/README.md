# Count the number of substrings with dominant ones

[Problem link](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [-1] + [i for i, c in enumerate(s) if c == '0'] + [n]

        z, Z = 0, len(zeros)
        ret = 0
        for i in range(n):
            while zeros[z] < i:
                z += 1
            for j in range(z, Z):
                if zeros[j] == i:
                    continue
                bad = j - z
                good = zeros[j] - i - bad
                ret += max(min(good - bad * bad + 1,
                           zeros[j] - max(i, zeros[j - 1])), 0)
                if i + (bad + 1) ** 2 >= n:
                    break
        return ret
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
