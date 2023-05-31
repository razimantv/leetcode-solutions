# Shortest path in a grid with obstacles elimination

[Problem link](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution {
 public:
  int shortestPath(vector<vector<int>>& grid, int k) {
    int m = grid.size(), n = grid[0].size();
    if (m == 1 and n == 1) return 0;

    vector<vector<vector<int>>> dist(
        m, vector<vector<int>>(n, vector<int>(k + 1, -1)));
    dist[0][0][k] = 0;
    queue<tuple<int, int, int>> bfsq;
    bfsq.push({0, 0, k});

    int neigh[4][2]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    while (!bfsq.empty()) {
      auto [i, j, rem] = bfsq.front();
      bfsq.pop();
      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj, rrem;
        if (ii >= 0 and ii < m and jj >= 0 and jj < n and
            (rrem = rem - grid[ii][jj]) >= 0 and dist[ii][jj][rrem] == -1) {
          dist[ii][jj][rrem] = dist[i][j][rem] + 1;
          if (ii == m - 1 and jj == n - 1) return dist[ii][jj][rrem];
          bfsq.push({ii, jj, rrem});
        }
      }
    }
    return -1;
  }
};
```