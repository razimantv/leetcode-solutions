# Minimum moves to spread stones over grid

[Problem link](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution {
 public:
  int minimumMoves(vector<vector<int>>& grid) {
    vector<pair<int, int>> donor, acceptor;
    for (int i = 0; i < 3; ++i)
      for (int j = 0; j < 3; ++j) {
        if (!grid[i][j]) {
          acceptor.push_back({i, j});
        } else if (grid[i][j] > 1) {
          for (int s = 1; s < grid[i][j]; ++s) donor.push_back({i, j});
        }
      }

    int n = donor.size(), best = 100;
    do {
      int cur{};
      for (int i = 0; i < n; ++i)
        cur += abs(donor[i].first - acceptor[i].first) +
               abs(donor[i].second - acceptor[i].second);
      best = min(best, cur);
    } while (next_permutation(donor.begin(), donor.end()));
    return best;
  }
};
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
