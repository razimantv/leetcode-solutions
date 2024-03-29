# Minimum changes to make k semi palindromes

[Problem link](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        facs = [[] for _ in range(n+1)]
        for i in range(1, n):
            for j in range(2*i, n+1, i):
                facs[j].append(i)

        cost = [[n for j in range(n)] for i in range(n)]
        for r in range(n):
            for l in range(r+1):
                L = r-l+1
                for x in facs[L]:
                    cur = 0
                    for y in range(x):
                        i = l + y
                        j = i + L - x
                        while i < j:
                            if s[i] != s[j]:
                                cur += 1
                            i += x
                            j -= x
                    cost[l][r] = min(cost[l][r], cur)

        dp = [[n for j in range(k+1)] for i in range(n+1)]
        dp[0][0] = 0
        for r in range(n):
            for j in range(1, k+1):
                for l in range(r+1):
                    dp[r+1][j] = min(dp[r+1][j], dp[l][j-1] + cost[l][r])
        return dp[-1][-1]
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Prime sieving](/README.md#Mathematics-Number_theory-Prime_sieving)
* [Palindrome](/README.md#Palindrome)
* [Dynamic programming](/README.md#Dynamic_programming) > [Auxiliary array](/README.md#Dynamic_programming-Auxiliary_array)
