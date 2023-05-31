# Search a 2d matrix ii

[Problem link](https://leetcode.com/problems/search-a-2d-matrix-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
 public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    for (int i = 0, m = matrix.size(), n = matrix[0].size(), j = n - 1;
         i < m and j >= 0; ++i) {
      while (j >= 0 and matrix[i][j] > target) --j;
      if (j >= 0 and matrix[i][j] == target) return true;
    }
    return false;
  }
};
```