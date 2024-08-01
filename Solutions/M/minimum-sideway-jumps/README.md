# Minimum sideway jumps

[Problem link](https://leetcode.com/problems/minimum-sideway-jumps)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-sideway-jumps

class Solution {
 public:
  int minSideJumps(vector<int>& obstacles) {
    int N = obstacles.size();
    vector<vector<int>> DP(N, vector<int>(3));
    DP[0][0] = DP[0][2] = 1;
    for (int i = 1; i < N; ++i) {
      for (int j = 0; j < 3; ++j) {
        if (obstacles[i] == j + 1)
          DP[i][j] = N + 1;
        else {
          DP[i][j] = DP[i - 1][j];
          if (obstacles[i - 1] != j + 1)
            DP[i][j] = min(DP[i][j], DP[i - 1][(j + 1) % 3] + 1);
          if (obstacles[i - 1] != j + 1)
            DP[i][j] = min(DP[i][j], DP[i - 1][(j + 2) % 3] + 1);
        }
      }
    }
    auto ret = DP.back();
    return min(ret[0], min(ret[1], ret[2]));
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
