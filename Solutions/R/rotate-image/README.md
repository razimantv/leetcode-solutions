# Rotate image

[Problem link](https://leetcode.com/problems/rotate-image)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rotate-image

class Solution {
 public:
  // i=0, ii=3, j=1, jj=2
  // 0,1 2,0 3,2 1,3
  void rotate(vector<vector<int>>& M) {
    int n = M.size();
    for (int i = 0, ii = n - 1; i <= ii; ++i, --ii)
      for (int j = 0, jj = n - 1; j < jj; ++j, --jj) {
        int temp = M[i][j];
        M[i][j] = M[jj][i];
        M[jj][i] = M[ii][jj];
        M[ii][jj] = M[j][ii];
        M[j][ii] = temp;
      }
    return;
  }
};
```