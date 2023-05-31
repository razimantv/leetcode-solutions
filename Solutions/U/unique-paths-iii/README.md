# Unique paths iii

[Problem link](https://leetcode.com/problems/unique-paths-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-paths-iii

class Solution {
  int cnt{0}, ans{0}, M, N;
  vector<vector<int>> dr;

 public:
  void work(vector<vector<int>>& grid, int i, int j) {
    if (cnt == 1) {
      ++ans;
      return;
    }
    if (grid[i][j] == 2) return;

    int temp = grid[i][j];
    grid[i][j] = -1;
    --cnt;
    for (const auto& dxy : dr) {
      int ii = i + dxy[0], jj = j + dxy[1];
      if (ii < 0 or ii >= M or jj < 0 or jj >= N or grid[ii][jj] < 0) continue;
      work(grid, ii, jj);
    }
    grid[i][j] = temp;
    ++cnt;
  }
  int uniquePathsIII(vector<vector<int>>& grid) {
    int sx, sy;
    M = grid.size(), N = grid[0].size();
    for (int i = 0; i < M; ++i)
      for (int j = 0; j < N; ++j) {
        int e = grid[i][j];
        if (e >= 0) ++cnt;
        if (e == 1) sx = i, sy = j;
      }

    dr = vector<vector<int>>{{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
    work(grid, sx, sy);
    return ans;
  }
};
```