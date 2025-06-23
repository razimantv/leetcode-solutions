# Sum of k mirror numbers

[Problem link](https://leetcode.com/problems/sum-of-k-mirror-numbers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isgood(n):
            num = []
            while n:
                num.append(n % k)
                n //= k
            return num == num[::-1]

        start, end, ret = 1, 10, 0
        while n:
            for skip in [1, 0]:
                for i in range(start, end):
                    s = str(i)
                    cur = int(s + s[::-1][skip:])
                    if isgood(cur):
                        ret += cur
                        n -= 1
                        if not n:
                            return ret
            start, end = end, end * 10
        return ret
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
