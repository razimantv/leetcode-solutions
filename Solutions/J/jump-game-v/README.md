# Jump game v

[Problem link](https://leetcode.com/problems/jump-game-v/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/jump-game-v/

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache 
        def dp(i):
            ret = 1
            for j in range(i-1, max(i-d-1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                ret = max(ret, 1 + dp(j))
            for j in range(i+1, min(i+d+1, n)):
                if arr[j] >= arr[i]:
                    break
                ret = max(ret, 1 + dp(j))
            return ret

        return max(dp(i) for i in range(n))
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
