# Sum of good subsequences

[Problem link](https://leetcode.com/problems/sum-of-good-subsequences/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-of-good-subsequences/

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        cnt, tot = defaultdict(int), defaultdict(int)
        ret, mod = 0, 10 ** 9 + 7

        for x in nums:
            newcnt = (1 + cnt[x - 1] + cnt[x + 1]) % mod
            newtot = (tot[x - 1] + tot[x + 1] + x * newcnt) % mod
            ret = (ret + newtot) % mod
            cnt[x] = (cnt[x] + newcnt) % mod
            tot[x] = (tot[x] + newtot) % mod
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
