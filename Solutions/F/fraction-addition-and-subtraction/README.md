# Fraction addition and subtraction

[Problem link](https://leetcode.com/problems/fraction-addition-and-subtraction/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)

        def getpair(s, i):
            sgn, numden = 1, [0, 0]
            if s[i] == '-':
                sgn = -1
                i += 1
            for j in [0, 1]:
                while i < n and s[i] not in '+-/':
                    numden[j] = numden[j] * 10 + int(s[i])
                    i += 1
                if i < n and s[i] != '-':
                    i += 1
            return i, sgn * numden[0], numden[1]

        i, retnum, retden = 0, 0, 1
        while i < n:
            i, num, den = getpair(expression, i)
            retnum, retden = retnum * den + num * retden, retden * den
            g = math.gcd(retnum, retden)
            retnum, retden = (retnum // g, retden // g) if g else (0, 1)
        return f'{retnum}/{retden}'
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
