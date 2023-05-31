# Swim in rising water

[Problem link](https://leetcode.com/problems/swim-in-rising-water)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/swim-in-rising-water

class Solution {
 public:
  vector<vector<char>> seen;
  const int neigh[4][2]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  bool connected(vector<vector<int>>& grid, int M, int N, int lim, int cur) {
    vector<pair<int, int>> stk{{0, 0}};
    seen[0][0] = cur;
    while (!stk.empty()) {
      auto [i, j] = stk.back();
      stk.pop_back();
      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj;
        if (ii == M - 1 and jj == N - 1) return true;
        if (ii >= 0 and jj >= 0 and ii < M and jj < N and
            grid[ii][jj] <= lim and seen[ii][jj] < cur) {
          seen[ii][jj] = cur;
          stk.push_back({ii, jj});
        }
      }
    }
    return false;
  }
  int swimInWater(vector<vector<int>>& grid) {
    int M = grid.size(), N = grid[0].size(),
        start = max(grid[0][0], grid[M - 1][N - 1]) - 1, end = M * N - 1,
        round = 0;
    seen = vector<vector<char>>(M, vector<char>(N));
    while (end - start > 1) {
      int mid = (end + start) >> 1;
      (connected(grid, M, N, mid, ++round) ? end : start) = mid;
    }
    return end;
  }
};
```