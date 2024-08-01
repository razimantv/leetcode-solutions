# Minimum cost to cut a stick

[Problem link](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution {
 public:
  int minCost(int n, vector<int>& cuts) {
    cuts.push_back(0);
    cuts.push_back(n);
    sort(cuts.begin(), cuts.end());

    int m = cuts.size();
    vector<vector<int>> dp(m, vector<int>(m));
    for (int L = 1; L < m; ++L) {
      for (int i = 0, j = i + L; j < m; ++i, ++j) {
        dp[i][j] = (L - 1) * (cuts[j] - cuts[i]);
        for (int k = i + 1; k < j; ++k)
          dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j]);
      }
    }
    return dp[0][m - 1];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
