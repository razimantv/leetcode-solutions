# Count substrings divisible by last digit

[Problem link](https://leetcode.com/problems/count-substrings-divisible-by-last-digit/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt9, cnt7 = [1] + [0] * 8, [[0] * 7 for _ in range(6)]
        cnt7[5][0] = 1
        pref9, pref7, ret = 0, 0, 0
        pow3, pow5 = [1, 3, 2, 6, 4, 5], [1, 5, 4, 6, 2, 3]
        for i, x in enumerate(s):
            d = int(x)
            pref9 = (pref9 + d) % 9
            pref7 = (pref7 * 3 + d) % 7
            if d in [1, 2, 5]:
                ret += i + 1
            elif d == 4:
                ret += 1
                if i and (int(s[i - 1:i + 1]) & 3 == 0):
                    ret += i
            elif d == 8:
                ret += 1
                if i and (int(s[i - 1:i + 1]) & 7 == 0):
                    ret += 1
                if i > 1 and (int(s[i - 2:i + 1]) & 7 == 0):
                    ret += i - 1
            elif d == 9:
                ret += cnt9[pref9]
            elif d in [3, 6]:
                ret += sum(cnt9[(pref9 + a) % 9] for a in [0, 3, 6])
            elif d == 7:
                for j in range(6):
                    ret += cnt7[j][(pref7 * pow3[j] * pow5[i % 6]) % 7]
            cnt9[pref9] += 1
            cnt7[i % 6][pref7] += 1
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Divisibility](/Collections/mathematics.md#divisibility)
