# Find the closest palindrome

[Problem link](https://leetcode.com/problems/find-the-closest-palindrome/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-closest-palindrome/

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        h1, h2 = (l + 1) // 2, l // 2
        best = 10 ** 19

        for delta in [-1, 0, 1]:
            left = str(int(n[:h1]) + delta)
            if left == '0':
                left = ''
            if len(left) < h2:
                cur = left + '9' + left[::-1]
            else:
                cur = left + left[:h2][::-1]
            if not cur:
                cur = '0'
            if cur != n and abs(int(n) - int(cur)) < best:
                ret, best = cur, abs(int(n) - int(cur))
        return ret
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
