# Spiral matrix ii

[Problem link](https://leetcode.com/problems/spiral-matrix-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/spiral-matrix-ii

class Solution {
 public:
  vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> step{{0, 1}, {1, 0}, {0, -1}, {-1, 0}},
        ret(n, vector<int>(n));
    for (int x = 0, i = 0, j = 0, d = 0; x < n * n;) {
      ret[i][j] = ++x;
      int ii = i + step[d][0], jj = j + step[d][1];
      if (ii < 0 or ii >= n or jj < 0 or jj >= n or ret[ii][jj]) {
        d = (d + 1) & 3;
        ii = i + step[d][0], jj = j + step[d][1];
      }
      i = ii;
      j = jj;
    }
    return ret;
  }
};
```