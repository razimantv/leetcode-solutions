# Most stones removed with same row or column

[Problem link](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column

class Solution {
 public:
  void dfs(vector<vector<int>>& stones, int i, int n) {
    auto& stone = stones[i];
    int x = stone[0], y = stone[1];
    stone = {};

    for (int j = 0; j < n; ++j) {
      auto& stone = stones[j];
      if (stone.empty()) continue;
      int xx = stone[0], yy = stone[1];
      if (xx == x or yy == y) dfs(stones, j, n);
    }
  }
  int removeStones(vector<vector<int>>& stones) {
    int n = stones.size(), c{};
    for (int i = 0; i < n; ++i) {
      if (stones[i].empty()) continue;
      ++c;
      dfs(stones, i, n);
    }
    return n - c;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
