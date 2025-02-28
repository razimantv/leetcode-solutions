# Shortest common supersequence

[Problem link](https://leetcode.com/problems/shortest-common-supersequence/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-common-supersequence/


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        cache = [[-1] * (n + 1) for _ in range(m + 1)]

        def work(i, j):
            if cache[i][j] != -1:
                return cache[i][j]

            if i == m:
                ret = n - j
            elif j == n:
                ret = m - i
            elif str1[i] == str2[j]:
                ret = 1 + work(i + 1, j + 1)
            else:
                ret = 1 + min(work(i, j + 1), work(i + 1, j))
            cache[i][j] = ret
            return ret

        i, j, ret = 0, 0, []
        while i < m or j < n:
            if i == m:
                ret.append(str2[j:])
                j = n
            elif j == n:
                ret.append(str1[i:])
                i = m
            elif str1[i] == str2[j]:
                ret.append(str1[i])
                i += 1
                j += 1
            elif work(i + 1, j) < work(i, j + 1):
                ret.append(str1[i])
                i += 1
            else:
                ret.append(str2[j])
                j += 1
        return ''.join(ret)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest common subsequence](/Collections/dynamic-programming.md#longest-common-subsequence)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Reconstructing optimal solution](/Collections/dynamic-programming.md#reconstructing-optimal-solution)
