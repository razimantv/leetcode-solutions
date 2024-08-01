# Get biggest three rhombus sums in a grid

[Problem link](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid

class Solution {
 public:
  vector<int> getBiggestThree(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();

    set<int> best;
    for (auto& r : grid)
      for (int x : r) best.insert(x);

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        for (int l = 1; l <= i and l <= j and i + l < m and j + l < n; ++l) {
          int cur = 0;
          for (int k = 0; k < l; ++k) {
            cur += grid[i + l - k][j + k] + grid[i - k][j + l - k] +
                   grid[i - l + k][j - k] + grid[i + k][j - l + k];
          }
          best.insert(cur);
        }

    int cnt = 0;
    vector<int> ret;
    for (auto mit = best.rbegin(); mit != best.rend() and cnt < 3; ++mit, ++cnt)
      ret.push_back(*mit);
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements)
* [Matrix](/Collections/matrix.md#matrix) > [Traversal](/Collections/matrix.md#traversal)
