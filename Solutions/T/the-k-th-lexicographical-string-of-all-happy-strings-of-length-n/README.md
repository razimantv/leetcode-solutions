# The k th lexicographical string of all happy strings of length n

[Problem link](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * 2 ** (n - 1) < k:
            return ''
        k -= 1
        ret = ''
        for i in range(n):
            poss = [c for c in 'abc' if not ret or ret[-1] != c]
            rest = 2 ** (n - 1 - i)
            cur = k // rest
            ret += poss[cur]
            k -= rest * cur
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
