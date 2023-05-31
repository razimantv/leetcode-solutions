# Pascals triangle ii

[Problem link](https://leetcode.com/problems/pascals-triangle-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/pascals-triangle-ii

class Solution {
 public:
  vector<int> getRow(int n) {
    vector<int> ret(n + 1);
    ret[0] = ret[n] = 1;
    for (int i = 1; 2 * i <= n; ++i) {
      ret[i] = (int)(((long long)ret[i - 1]) * (n - i + 1) / i);
      ret[n - i] = ret[i];
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Array reuse](/README.md#Dynamic_programming-Array_reuse)
