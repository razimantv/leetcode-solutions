# Paint house iii

[Problem link](https://leetcode.com/problems/paint-house-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/paint-house-iii

class Solution {
 public:
  int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n,
              int target) {
    // DP[i][j][k] = minimum cost of colouring first i cells 
    // such that last cell is coloured jand there are k overall

    const int INF = 1'000'000'000;
    vector<vector<vector<int>>> DP(
        m, vector<vector<int>>(n, vector<int>(target + 1, INF)));
    if (houses[0]--)
      DP[0][houses[0]][1] = 0;
    else {
      for (int i = 0; i < n; ++i) DP[0][i][1] = cost[0][i];
    }

    for (int i = 1; i < m; ++i) {
      if (houses[i]--) {
        for (int j = 1; j <= target; ++j) {
          int& cur = DP[i][houses[i]][j];
          cur = DP[i - 1][houses[i]][j];
          for (int k = 0; k < n; ++k)
            if (k != houses[i]) cur = min(cur, DP[i - 1][k][j - 1]);
        }
      } else {
        for (int c = 0; c < n; ++c) {
          for (int j = 1; j <= target; ++j) {
            int& cur = DP[i][c][j];
            cur = DP[i - 1][c][j] + cost[i][c];
            for (int k = 0; k < n; ++k)
              if (k != c) cur = min(cur, DP[i - 1][k][j - 1] + cost[i][c]);
          }
        }
      }
    }

    int best = INF;
    for (int c = 0; c < n; ++c) best = min(best, DP[m - 1][c][target]);
    return (best == INF) ? -1 : best;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
