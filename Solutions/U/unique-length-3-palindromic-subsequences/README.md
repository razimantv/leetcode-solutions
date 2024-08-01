# Unique length 3 palindromic subsequences

[Problem link](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        left = [0] * n
        for i in range(n-1):
            left[i+1] = left[i] | (1 << (ord(s[i])-ord('a')))
        right = 0
        good = [0] * 676
        for i in range(n-1, -1, -1):
            cur = ord(s[i]) - ord('a')
            mask = left[i] & right
            for b in range(26):
                if mask & (1 << b):
                    good[b * 26 + cur] = 1
            right |= (1 << cur)

        return sum(good)
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
* [Prefix](/Collections/prefix.md#prefix) > [Bitwise operation](/Collections/prefix.md#bitwise-operation)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Palindrome](/Collections/palindrome.md#palindrome)
