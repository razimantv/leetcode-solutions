# Range addition ii

[Problem link](https://leetcode.com/problems/range-addition-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-addition-ii

class Solution {
 public:
  int maxCount(int m, int n, vector<vector<int>>& ops) {
    for (auto& v : ops) m = min(m, v[0]), n = min(n, v[1]);
    return m * n;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
