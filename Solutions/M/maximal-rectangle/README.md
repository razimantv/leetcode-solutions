# Maximal rectangle

[Problem link](https://leetcode.com/problems/maximal-rectangle)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximal-rectangle

class Solution {
 public:
  int maximalRectangle(vector<vector<char>>& s) {
    if (s.empty()) return 0;

    int m = s.size(), n = s[0].size();
    vector<vector<unsigned char>> matrix(m, vector<unsigned char>(n));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) matrix[i][j] = s[i][j] - '0';

    for (int i = 1; i < m; ++i)
      for (int j = 0; j < n; ++j) matrix[i][j] += matrix[i - 1][j];

    int ret = 0;
    for (int i = 0; i < m; ++i)
      for (int j = i; j < m; ++j) {
        int h = j - i + 1, cur = 0;
        for (int k = 0; k < n; ++k) {
          int tot = matrix[j][k];
          if (i) tot -= matrix[i - 1][k];
          if (tot == h)
            ret = max(ret, cur += h);
          else
            cur = 0;
          // cout<<i<<" "<<j<<" "<<k<<" "<<tot<<"\n";
        }
      }
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
