# Selling pieces of wood

[Problem link](https://leetcode.com/problems/selling-pieces-of-wood)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/selling-pieces-of-wood

class Solution {
 public:
  long long sellingWood(int m, int n, const vector<vector<int>>& prices) {
    vector<vector<long long>> best(m + 1, vector<long long>(n + 1));
    for (auto u : prices) best[u[0]][u[1]] = u[2];
    for (int i = 1; i <= m; ++i)
      for (int j = 1; j <= n; ++j) {
        for (int k = 1, kk = i - 1; k <= kk; ++k, --kk)
          best[i][j] = max(best[i][j], best[k][j] + best[kk][j]);
        for (int k = 1, kk = j - 1; k <= kk; ++k, --kk)
          best[i][j] = max(best[i][j], best[i][k] + best[i][kk]);
      }
    return best[m][n];
  }
};
```