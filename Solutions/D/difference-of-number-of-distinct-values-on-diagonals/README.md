# Difference of number of distinct values on diagonals

[Problem link](https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution {
 public:
  vector<vector<int>> differenceOfDistinctValues(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> ret(m, vector<int>(n));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        unordered_set<int> tl, br;
        for (int ii = i - 1, jj = j - 1; ii >= 0 and jj >= 0; --ii, --jj)
          tl.insert(grid[ii][jj]);
        for (int ii = i + 1, jj = j + 1; ii < m and jj < n; ++ii, ++jj)
          br.insert(grid[ii][jj]);
        ret[i][j] = abs((int)tl.size() - (int)br.size());
      }
    return ret;
  }
};
```
## Tags

* [Matrix](/Collections/matrix.md#matrix)
* [Hashmap](/Collections/hashmap.md#hashmap)
