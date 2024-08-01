# Row with maximum ones

[Problem link](https://leetcode.com/problems/row-with-maximum-ones/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
 public:
  vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
    int pos, val{-1};
    for (int i = 0, n = mat.size(); i < n; ++i) {
      int cur = accumulate(mat[i].begin(), mat[i].end(), 0);
      if (cur > val) val = cur, pos = i;
    }
    return {pos, val};
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
