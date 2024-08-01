# Maximum rows covered by columns

[Problem link](https://leetcode.com/problems/maximum-rows-covered-by-columns/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution {
 public:
  int covered(vector<vector<int>>& mat, int m, int n, int mask) {
    int badrowmask = 0;
    for (int i = 0; i < n; ++i, mask >>= 1) {
      if (mask & 1) continue;
      for (int j = 0; j < m; ++j)
        if (mat[j][i]) badrowmask |= (1 << j);
    }
    return m - __builtin_popcount(badrowmask);
  }
  int maximumRows(vector<vector<int>>& mat, int cols) {
    int m = mat.size(), n = mat[0].size(), best = 0;
    for (int i = 0; i < (1 << n); ++i)
      if (__builtin_popcount(i) == cols)
        best = max(best, covered(mat, m, n, i));
    return best;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
