# Stone game v

[Problem link](https://leetcode.com/problems/stone-game-v/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stone-game-v/

class Solution {
  vector<vector<int>> memo;
  vector<int> psum;

  int dp(int l, int r) {
    if (l == r)
      return 0;

    if (memo[l][r] != -1)
      return memo[l][r];

    int max_score = 0;

    for (int m = l; m < r; ++m) {
      int lsum = psum[m + 1] - psum[l], rsum = psum[r + 1] - psum[m + 1];

      if (lsum < rsum) {
        max_score = max(max_score, lsum + dp(l, m));
      } else if (rsum < lsum) {
        max_score = max(max_score, rsum + dp(m + 1, r));
      } else {
        max_score = max(max_score, lsum + max(dp(l, m), dp(m + 1, r)));
      }
    }

    return memo[l][r] = max_score;
  }

public:
  int stoneGameV(vector<int> &stones) {
    int n = stones.size();
    memo.assign(n, vector<int>(n, -1));

    psum.assign(n + 1, 0);
    for (int i = 0; i < n; ++i)
      psum[i + 1] = psum[i] + stones[i];

    return dp(0, n - 1);
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/stone-game-v/

class Solution:
    def stoneGameV(self, stones: list[int]) -> int:
        n = len(stones)
        dp, dp1, dp2 = [[[0] * n for _ in range(n)] for d in range(3)]
        psum = list(accumulate(stones, initial=0))
        for i in range(n):
            dp1[i][i] = dp2[i][i] = stones[i]

        for L in range(2, n + 1):
            l, m, r = 0, 0, L - 1
            while r < n:
                while psum[m + 1] - psum[l] <= psum[r + 1] - psum[m + 1]:
                    m += 1
                m1 = m - 1
                m2 = m if psum[r + 1] - psum[m] == psum[m] - psum[l] else m + 1
                dp[l][r] = max(
                    dp1[l][m1] if m1 >= l else 0, dp2[m2][r] if m2 <= r else 0
                )
                dp1[l][r] = max(
                    dp1[l][r - 1], dp[l][r] + psum[r + 1] - psum[l]
                )
                dp2[l][r] = max(
                    dp2[l + 1][r], dp[l][r] + psum[r + 1] - psum[l]
                )

                l, r = l + 1, r + 1

        return dp[0][-1]
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
