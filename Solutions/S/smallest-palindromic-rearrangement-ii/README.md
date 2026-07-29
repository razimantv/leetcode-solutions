# Smallest palindromic rearrangement ii

[Problem link](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        
        mid, ctr = '', Counter(s)
        for c in sorted(ctr):
            if ctr[c] & 1:
                mid = c
            ctr[c] //= 2

        n, keys = sum(ctr.values()), sorted(ctr. keys())

        def perms(ctr, n, target):
            if target <= 1: 
                return 0
            ret = 1
            for v in ctr.values():
                vv = v
                if v * 2 > n:
                    v = n - v
                for i in range(1, v + 1):
                    ret = (ret * (n + 1 - i)) // i
                    if ret >= target: 
                        return 0
                n -= vv
            return ret

        if perms(ctr, n, k):
            return ''

        left = []
        while n:
            n -= 1
            for key in keys:
                if not ctr[key]:
                    continue
                ctr[key] -= 1
                p = perms(ctr, n, k)
                if not p:
                    left.append(key)
                    break
                ctr[key] += 1
                k -= p
        ret = ''. join(left) 
        return ret + mid + ret[::-1]
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [nth](/Collections/permutation.md#nth)
* [Palindrome](/Collections/palindrome.md#palindrome)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
