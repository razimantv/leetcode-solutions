# Delete columns to make sorted

[Problem link](https://leetcode.com/problems/delete-columns-to-make-sorted/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution {
 public:
  int minDeletionSize(vector<string>& strs) {
    int m = strs.size(), n = strs[0].size();
    int ret{};
    for (int c = 0; c < n; ++c) {
      for (int i = 1; i < m; ++i)
        if (strs[i][c] < strs[i - 1][c]) {
          ++ret;
          break;
        }
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
