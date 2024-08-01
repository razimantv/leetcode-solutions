# Champagne tower

[Problem link](https://leetcode.com/problems/champagne-tower)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/champagne-tower

class Solution {
 public:
  double champagneTower(int poured, int query_row, int query_glass) {
    vector<double> state(query_row + 1);
    state[0] = poured;
    for (int i = 0; i < query_row; ++i)
      for (int j = i; j >= 0; --j) {
        state[j] = max(0., state[j] - 1);
        state[j + 1] += state[j] /= 2;
      }
    return min(1., state[query_glass]);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
