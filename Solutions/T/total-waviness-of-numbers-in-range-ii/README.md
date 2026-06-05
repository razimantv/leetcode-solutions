# Total waviness of numbers in range ii

[Problem link](https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def sign(prev, cur):
            return 1 if prev > cur else -1 if prev < cur else 0
            
        @cache
        def dp(d, prev, p):
		   # If current digit is d and previous digit status is prev (-1/0/1),
           # how much waviness can be achieved with p more positions? 
            if not p:
                return 0
            ret = 0
            if prev == 1:
                ret = (9 - d) * (10 ** (p - 1))
            elif prev == -1:
                ret = d * (10 ** (p - 1))
            for next in range(10):
                ret += dp(next, sign(d, next), p - 1)

            return ret

        @cache
        def dp2(p):
            # Total waviness of numbers up to p digits
            if p < 3:
                return 0
            return dp2(p - 1) + sum(dp(d, 0, p - 1) for d in range(1, 10)

        def work(n):
            if n < 101:
                return 0

            digs = list(map(int, str(n)))
            prev, d, cnt, L = 0, 0, 0, len(digs)
            ret = dp2(L - 1)
            for i in range(L):
                for cur in range(i == 0, digs[i]):
                    add = 1 if (
                        (prev == 1 and cur > d) or (prev == -1 and cur < d)
                    ) else 0
                    ret += (cnt + add) * (10 ** (L - 1 - i)) + dp(
                        cur, sign(d, cur) if i else 0, L - 1 - i
                    )
                cnt +=  1 if (
                    (prev == 1 and digs[i] > d) or (prev == -1 and  digs[i] < d)
                ) else 0
                prev, d = sign(d, digs[i]) if i else 0, digs[i]

            return ret

        return work(num2 + 1) - work(num1)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
