# Length of longest fibonacci subsequence

[Problem link](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        inv = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        cache = [[-1] * n for _ in range(n)]

        def dp(i, j):
            if cache[i][j] != -1:
                return cache[i][j]
            next = arr[i] + arr[j]
            cache[i][j] = (1 + dp(j, inv[next])) if next in inv else 2
            return cache[i][j]

        ret = max(dp(i, j) for j in range(n) for i in range(j))
        return 0 if ret < 3 else ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
