# Largest plus sign

[Problem link](https://leetcode.com/problems/largest-plus-sign)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-plus-sign

class Solution {
 public:
  int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
    short best = 0;
    vector<vector<short>> l(n, vector<short>(n, 1)), u, r, d;
    for (auto& m : mines) l[m[0]][m[1]] = 0;
    u = r = d = l;

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        if (i and l[i][j]) l[i][j] += l[i - 1][j];
        if (j and u[i][j]) u[i][j] += u[i][j - 1];
      }

    for (int i = n - 1; i >= 0; --i)
      for (int j = n - 1; j >= 0; --j) {
        if (i < n - 1 and r[i][j]) r[i][j] += r[i + 1][j];
        if (j < n - 1 and d[i][j]) d[i][j] += d[i][j + 1];
        best = max(best, min(min(r[i][j], l[i][j]), min(u[i][j], d[i][j])));
      }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
