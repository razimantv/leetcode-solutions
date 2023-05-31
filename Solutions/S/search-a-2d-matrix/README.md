# Search a 2d matrix

[Problem link](https://leetcode.com/problems/search-a-2d-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/search-a-2d-matrix

class Solution {
 public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    for (auto& r : matrix)
      for (int i : r)
        if (i == target) return true;
    return false;
  }
};
```