# Greatest common divisor of strings

[Problem link](https://leetcode.com/problems/greatest-common-divisor-of-strings)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        m = len(str1)
        n = len(str2)
        g = gcd(m, n)
        pref = str1[:g]
        return pref if pref * (m//g) == str1 and pref * (n//g) == str2 else ""
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
