# Determine whether matrix can be obtained by rotation

[Problem link](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation

class Solution {
 public:
  vector<vector<int>> rotate(vector<vector<int>>& mat) {
    int N = mat.size();
    auto ret = mat;
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j) ret[i][j] = mat[j][N - 1 - i];
    return ret;
  }
  bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
    for (int i = 0; i < 4; ++i) {
      if (mat == target) return true;
      mat = rotate(mat);
    }
    return false;
  }
};
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Geometric transformation](/Collections/matrix.md#geometric-transformation)
