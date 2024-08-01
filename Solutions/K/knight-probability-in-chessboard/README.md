# Knight probability in chessboard

[Problem link](https://leetcode.com/problems/knight-probability-in-chessboard/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution {
 public:
  double knightProbability(int n, int k, int row, int col) {
    const vector<pair<int, int>> neigh{{-1, -2}, {-2, -1}, {-1, 2}, {-2, 1},
                                       {1, -2},  {2, -1},  {1, 2},  {2, 1}};
    vector<vector<double>> prob(n, vector<double>(n));
    prob[row][col] = 1;
    while (k--) {
      vector<vector<double>> next(n, vector<double>(n));
      for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
          for (auto [di, dj] : neigh) {
            int ii = i + di, jj = j + dj;
            if (ii >= 0 and ii < n and jj >= 0 and jj < n)
              next[ii][jj] += prob[i][j] / 8;
          }
      prob = next;
    }

    double ret{};
    for (const auto& row : prob)
      for (double x : row) ret += x;
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
