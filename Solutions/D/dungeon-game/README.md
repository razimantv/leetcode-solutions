# Dungeon game

[Problem link](https://leetcode.com/problems/dungeon-game)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/dungeon-game

class Solution {
 public:
  bool poss(vector<vector<int>> d, int h) {
    for (int i = 0; i < d.size(); ++i) {
      for (int j = 0; j < d[0].size(); ++j) {
        int best = (i + j == 0) ? h : 0;
        if (i > 0) best = max(best, d[i - 1][j]);
        if (j > 0) best = max(best, d[i][j - 1]);
        if (best > 0)
          d[i][j] += best;
        else
          d[i][j] = 0;
      }
    }
    return d.back().back() > 0;
  }

  int calculateMinimumHP(vector<vector<int>>& dungeon) {
    int start = max(0, -dungeon[0][0]), end = 1;
    for (auto& v : dungeon)
      for (auto e : v) end -= min(0, e);
    while (end - start > 1) {
      int mid = (end + start) / 2;
      if (poss(dungeon, mid))
        end = mid;
      else
        start = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
