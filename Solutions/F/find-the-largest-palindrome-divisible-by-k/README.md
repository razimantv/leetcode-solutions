# Find the largest palindrome divisible by k

[Problem link](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        powk = [1] * (n + 1)
        for i in range(n):
            powk[i + 1] = (powk[i] * 10) % k

        lmid, rmid = (n - 1) // 2, n // 2
        poss = [[False] * k for _ in range(lmid + 2)]
        if lmid != rmid:
            poss[lmid + 1][0] = True

        l, r = lmid, rmid
        while l >= 0:
            if l == r:
                for d in range(10):
                    poss[l][(powk[l] * d) % k] = True
            else:
                cur = list(set(
                    ((powk[l] + powk[r]) * d) % k
                    for d in range(l == 0 and n > 1, 10)
                ))
                for x in range(k):
                    for y in cur:
                        if poss[l + 1][(x + k - y) % k]:
                            poss[l][x] = True
                            break
            l, r = l - 1, r + 1

        ret = [''] * n
        l, r, rem = 0, n - 1, 0
        while l <= r:
            if l == r:
                for d in range(9, -1, -1):
                    if (d * powk[l]) % k == rem:
                        ret[l] = str(d)
                        break
                break
            for d in range(9, (l == 0 and n > 1) - 1, -1):
                cur = ((powk[l] + powk[r]) * d) % k
                next = (rem + k - cur) % k
                if poss[l + 1][next]:
                    ret[l] = ret[r] = str(d)
                    rem = next
                    break
            l, r = l + 1, r - 1
        return ''.join(ret)
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Construction](/Collections/construction.md#construction)
* [Greedy](/Collections/greedy.md#greedy)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
