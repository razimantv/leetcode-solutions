# Non decreasing array

[Problem link](https://leetcode.com/problems/non-decreasing-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/non-decreasing-array

class Solution {
 public:
  bool checkPossibility(vector<int>& a) {
    for (int i = 1, n = a.size(), bad = 0; i < n; ++i) {
      if (a[i] >= a[i - 1]) continue;
      if (bad++) return false;
      if (i < 2 or a[i - 2] <= a[i])
        a[i - 1] = a[i];
      else
        a[i] = a[i - 1];
    }
    return true;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
