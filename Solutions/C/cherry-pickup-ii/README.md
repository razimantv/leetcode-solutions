# Cherry pickup ii

[Problem link](https://leetcode.com/problems/cherry-pickup-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/cherry-pickup-ii

class Solution {
 public:
  int cherryPickup(vector<vector<int>>& grid) {
    int M = grid.size(), N = grid[0].size();
    vector<vector<int>> cur(N, vector<int>(N, -1000000000)), prev{cur};
    cur[0][N - 1] = grid[0][0] + grid[0][N - 1];

    int best = 0;
    for (int i = 1; i < M; ++i) {
      cur.swap(prev);
      for (int j = 0; j < N; ++j)
        for (int k = j + 1; k < N; ++k) {
          cur[j][k] = -1000000000;
          for (int dj = -1; dj <= 1; ++dj)
            for (int dk = -1; dk <= 1; ++dk) {
              if (j + dj >= 0 and j + dj < k + dk and k + dk < N)
                cur[j][k] = max(cur[j][k], prev[j + dj][k + dk]);
            }
          best = max(best, cur[j][k] += grid[i][j] + grid[i][k]);
        }
    }
    return best;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
