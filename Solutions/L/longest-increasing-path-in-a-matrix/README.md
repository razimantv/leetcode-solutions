# Longest increasing path in a matrix

[Problem link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution {
 public:
  int dp[205][205];
  int visited[205][205];
  int dx[4] = {1, -1, 0, 0};
  int dy[4] = {0, 0, 1, -1};
  void dfs(vector<vector<int>>& matrix, int r, int c) {
    if (r < 0 || c < 0 || r >= matrix.size() || c >= matrix[0].size() ||
        visited[r][c]) {
      return;
    }
    visited[r][c] = 1;
    for (int i = 0; i < 4; i++) {
      int nr = r + dx[i];
      int nc = c + dy[i];
      if (nr >= 0 && nc >= 0 && nr < matrix.size() && nc < matrix[0].size() &&
          matrix[nr][nc] > matrix[r][c]) {
        dfs(matrix, nr, nc);
        dp[r][c] = max(dp[r][c], dp[nr][nc] + 1);
      }
    }
  }

  int longestIncreasingPath(vector<vector<int>>& matrix) {
    int r = matrix.size();
    int c = matrix[0].size();

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        dp[i][j] = 1;
        visited[i][j] = 0;
      }
    }

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (!visited[i][j]) {
          dfs(matrix, i, j);
        }
      }
    }
    int ans = 0;

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        ans = max(ans, dp[i][j]);
      }
    }

    return ans;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
