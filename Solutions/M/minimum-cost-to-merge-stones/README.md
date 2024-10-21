# Minimum cost to merge stones

[Problem link](https://leetcode.com/problems/minimum-cost-to-merge-stones/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if k > 2 and n % (k - 1) != 1:
            return -1
        psum = [0] + list(accumulate(stones))
        
        # dp(i, j, p) = minimum cost to make j merges
        #               in the subarray starting with i
        #               to end up with p elements
        @cache
        def dp(i, j, p):
            if j == 0:
                return 0
            elif p == 1:
                return psum[i + j * (k - 1) + 1] - psum[i] + min(
                    dp(i, jj, 1) + dp(i + jj * (k - 1) + 1, j - 1 - jj, k - 1)
                    for jj in range(j)
                )
            return min(
                dp(i, jj, 1) + dp(i + jj * (k - 1) + 1, j - jj, p - 1)
                for jj in range(j + 1)
            )
        
        return dp(0, (n - 1) // (k - 1), 1)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
