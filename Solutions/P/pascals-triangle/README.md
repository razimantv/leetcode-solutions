# Pascals triangle

[Problem link](https://leetcode.com/problems/pascals-triangle)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/pascals-triangle

class Solution {
 public:
  vector<vector<int>> generate(int numRows) {
    vector<vector<int>> ret(numRows, {1});
    for (int i = 1; i < numRows; ++i) {
      for (int j = 1; j < i; ++j)
        ret[i].push_back(ret[i - 1][j] + ret[i - 1][j - 1]);
      ret[i].push_back(1);
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
