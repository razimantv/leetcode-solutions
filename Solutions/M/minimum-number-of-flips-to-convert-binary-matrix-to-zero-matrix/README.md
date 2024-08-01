# Minimum number of flips to convert binary matrix to zero matrix

[Problem link](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix

class Solution {
  int m, n;
  vector<int> flipmask;
  const vector<pair<int, int>> neigh{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

  int gen_flipmask(int i, int j) {
    int ret = (1 << (i * n + j));
    for (auto [di, dj] : neigh) {
      int ii = i + di, jj = j + dj;
      if (ii >= 0 and ii < m and jj >= 0 and jj < n)
        ret ^= (1 << (ii * n + jj));
    }
    return ret;
  }

  bool work(int mat, int mask) {
    for (int i = 0; i < (m * n); ++i, mask >>= 1)
      if (mask & 1) mat ^= flipmask[i];
    return !mat;
  }

  int mattoint(const vector<vector<int>>& mat) {
    int ret = 0;
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (mat[i][j]) ret ^= (1 << (i * n + j));
    return ret;
  }

 public:
  int minFlips(vector<vector<int>>& mat) {
    m = mat.size(), n = mat[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) flipmask.push_back(gen_flipmask(i, j));

    int best = m * n + 1, mat_int = mattoint(mat);
    for (int i = 0, cur; i < (1 << (m * n)); ++i) {
      if ((cur = __builtin_popcount(i)) < best and work(mat_int, i)) best = cur;
    }
    return (best <= m * n) ? best : -1;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Build result bit-by-bit](/Collections/bitwise-operation.md#build-result-bit-by-bit)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
