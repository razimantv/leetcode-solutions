# Largest magic square

[Problem link](https://leetcode.com/problems/largest-magic-square)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-magic-square

class Solution {
 public:
  bool ismagic(const vector<vector<int>>& grid, int i, int j, int L) {
    int tot = 0;
    for (int ii = i; ii < i + L; ++ii) {
      int cur = 0;
      for (int jj = j; jj < j + L; ++jj) cur += grid[ii][jj];
      if (tot and cur != tot) return false;
      tot = cur;
    }
    for (int jj = j; jj < j + L; ++jj) {
      int cur = 0;
      for (int ii = i; ii < i + L; ++ii) cur += grid[ii][jj];
      if (tot and cur != tot) return false;
      tot = cur;
    }
    {
      int cur = 0;
      for (int d = 0; d < L; ++d) cur += grid[i + d][j + d];
      if (tot and cur != tot) return false;
      tot = cur;
    }
    {
      int cur = 0;
      for (int d = 0; d < L; ++d) cur += grid[i + d][j + L - 1 - d];
      if (tot and cur != tot) return false;
      tot = cur;
    }
    return true;
  }
  int largestMagicSquare(vector<vector<int>>& grid) {
    int M = grid.size(), N = grid[0].size();
    int best = 1;
    for (int L = 1; L <= M and L <= N; ++L) {
      for (int i = 0; i + L <= M; ++i)
        for (int j = 0; j + L <= N; ++j) {
          if (ismagic(grid, i, j, L)) {
            best = L;
            goto BPP;
          }
        }

    BPP:;
    }
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
