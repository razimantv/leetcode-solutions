# Brick wall

[Problem link](https://leetcode.com/problems/brick-wall)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/brick-wall

class Solution {
 public:
  int leastBricks(vector<vector<int>>& wall) {
    unordered_map<int, int> cnt;
    for (auto& row : wall) {
      int prev = 0;
      for (int n : row) {
        if (prev) ++cnt[prev];
        prev += n;
      }
    }

    int best = 0;
    for (auto [v, c] : cnt) best = max(best, c);
    return wall.size() - best;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
