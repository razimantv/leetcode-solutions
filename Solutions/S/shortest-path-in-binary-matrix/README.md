# Shortest path in binary matrix

[Problem link](https://leetcode.com/problems/shortest-path-in-binary-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution {
 public:
  int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
    int N = grid.size();
    if (grid[0][0] or grid[N - 1][N - 1]) return -1;

    queue<pair<int, int>> bfsq;
    bfsq.push({0, 0});
    grid[0][0] = 1;

    vector<pair<int, int>> neigh{{-1, 0}, {1, 0},   {0, -1}, {0, 1},
                                 {-1, 1}, {-1, -1}, {1, 1},  {1, -1}};

    while (!bfsq.empty()) {
      auto [i, j] = bfsq.front();
      bfsq.pop();
      if (i == N - 1 and j == N - 1) return grid[i][j];

      for (auto [dx, dy] : neigh) {
        int ii = i + dx, jj = j + dy;
        if (ii < 0 or jj < 0 or ii >= N or jj >= N or grid[ii][jj]) continue;
        grid[ii][jj] = grid[i][j] + 1;
        bfsq.push({ii, jj});
      }
    }

    return -1;
  }
};
```