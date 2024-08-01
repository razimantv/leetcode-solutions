# Paths in matrix whose sum is divisible by k

[Problem link](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

class Solution {
 public:
  int numberOfPaths(vector<vector<int>>& grid, int k) {
    int m = grid.size(), n = grid[0].size();
    const int MOD = 1'000'000'007;
    vector<vector<int>> dp(n, vector<int>(k));
    dp[0][grid[0][0] % k] = 1;
    for (int i = 1, pref = grid[0][0]; i < n; ++i) {
      pref = (pref + grid[0][i]) % k;
      dp[i][pref] = 1;
    }
    for (int i = 1; i < m; ++i) {
      vector<vector<int>> newdp(n, vector<int>(k));
      for (int j = 0; j < k; ++j) {
        newdp[0][(j + grid[i][0]) % k] = dp[0][j];
      }
      for (int j = 1; j < n; ++j) {
        int cur = grid[i][j] % k;
        for (int kp = 0; kp < k; ++kp) {
          newdp[j][kp] =
              (newdp[j - 1][(kp + k - cur) % k] + dp[j][(kp + k - cur) % k]) %
              MOD;
        }
      }
      dp = newdp;
    }
    return dp.back()[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Grid](/Collections/dynamic-programming.md#grid)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
