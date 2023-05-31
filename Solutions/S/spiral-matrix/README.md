# Spiral matrix

[Problem link](https://leetcode.com/problems/spiral-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/spiral-matrix

class Solution {
 public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    int d[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    vector<int> ret;
    for (int i = 0, j = 0, m = matrix.size(), n = matrix[0].size(), print = 1,
             x = 0;
         ;) {
      if (print) {
        ret.push_back(matrix[i][j]);
        matrix[i][j] = 101;
      }
      int ii = i + d[x][0], jj = j + d[x][1];
      if (ii >= 0 and ii < m and jj >= 0 and jj < n and matrix[ii][jj] < 101)
        i = ii, j = jj, print = true;
      else if (!print)
        break;
      else
        print = 0, x = (x + 1) & 3;
    }
    return ret;
  }
};
```